"""Download every photo the site uses into assets/photos/ so the site no longer hotlinks
other websites. Already-downloaded photos are skipped. Writes content/photos.json
(original URL -> local path), which images.real_url() uses."""
import json, os, sys, time, urllib.request, mimetypes
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
os.environ["SANCHARI_NO_PHOTOS"] = "1"          # use original URLs while collecting
import data, images as IM
import build_consts  # extra one-off image URLs (e.g. video poster)

PHOTOS = os.path.join(ROOT, "assets", "photos")
MAP = os.path.join(ROOT, "content", "photos.json")
os.makedirs(PHOTOS, exist_ok=True)
mapping = json.load(open(MAP)) if os.path.exists(MAP) else {}

wanted = {}
for k in IM.REG:
    u = IM.real_url(k)
    if u and u.startswith("http"): wanted.setdefault(u, k)
for name, u in build_consts.EXTRA_PHOTOS.items(): wanted.setdefault(u, name)

EXT = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp", "image/gif": ".gif"}
UA = "SanchariSiteBuilder/1.0 (https://nreddyi.github.io/sanchari/; info@sanchari.travel)"
ok = skip = fail = 0
for url, key in wanted.items():
    if url in mapping and os.path.exists(os.path.join(ROOT, mapping[url])):
        skip += 1; continue
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                ctype = r.headers.get_content_type(); body = r.read()
            if not ctype.startswith("image/"): raise ValueError("not an image: " + ctype)
            ext = EXT.get(ctype) or mimetypes.guess_extension(ctype) or ".jpg"
            rel = f"assets/photos/{key}{ext}"
            with open(os.path.join(ROOT, rel), "wb") as f: f.write(body)
            mapping[url] = rel; ok += 1
            print(f"ok   {key:28s} {len(body)//1024:5d} KB  {url[:90]}")
            break
        except Exception as e:
            wait = 5 * (attempt + 1)
            print(f"retry {key} ({e}); waiting {wait}s"); time.sleep(wait)
    else:
        fail += 1; print(f"FAIL {key} {url}")
    time.sleep(0.4)
with open(MAP, "w") as f: json.dump(mapping, f, indent=1, sort_keys=True); f.write("\n")
print(f"downloaded {ok}, already had {skip}, failed {fail}")
