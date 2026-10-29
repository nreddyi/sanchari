"""One-off: write the tours currently defined in data.py to content/tours/*.json (CMS-editable)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
os.environ["SANCHARI_NO_JSON"] = "1"
import data, images as IM
OUT = os.path.join(os.path.dirname(__file__), "..", "content", "tours")
os.makedirs(OUT, exist_ok=True)
for i, t in enumerate(data.TOURS, 1):
    d = {
        "slug": t["slug"].replace("tour-", "", 1),
        "order": i,
        "title": t["title"], "short_name": t["short"],
        "category": t["cat"], "region": t["region"], "region_key": t["rkey"], "zone": t.get("zone", ""),
        "travel_styles": t.get("styles") or [],
        "featured": bool(t.get("featured")), "badge": t.get("badge") or "",
        "days": t["days"], "nights": t["nights"], "price": t["price"], "route": t["route"],
        "card_points": t["card"],
        "stats": [{"icon": a, "value": b, "label": c} for a, b, c in t["stats"]],
        "overview": t["overview"],
        "highlights": [{"title": a, "text": b} for a, b in t["highlights"]],
        "stops": t["stops"],
        "itinerary": [{"title": a, "subtitle": b, "intro": c, "activities": [{"time": x, "title": y, "text": z} for x, y, z in s], "draft": bool(dr)}
                      for a, b, c, s, dr in t["itinerary"]],
        "inclusions": t["incl"], "exclusions": t["excl"],
        "gallery": [{"image": IM.real_url(k) or f"assets/img/{k}.svg", "caption": IM.REG[k][0], "kind": IM.REG[k][1]} for k in t["images"]],
        "good_to_know": [{"title": a, "text": b} for a, b in t["know"]],
        "faqs": [{"question": a, "answer": b} for a, b in t["faq"]],
    }
    with open(os.path.join(OUT, d["slug"] + ".json"), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2); f.write("\n")
print("exported", len(data.TOURS))
