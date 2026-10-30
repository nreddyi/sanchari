# Sanchari Travel website

Live site: https://nreddyi.github.io/sanchari/

## Editing tours (dashboard)
1. Go to https://app.pagescms.org and sign in with GitHub.
2. Open **nreddyi/sanchari** → **Tour packages**.
3. Edit a tour (Overview, Itinerary, Inclusions, Gallery, Good to know, FAQs…) and click **Save**.
4. The site rebuilds automatically; changes are live in about 1–2 minutes.

## How it works
- `content/tours/*.json` — one file per tour (edited by the dashboard)
- `assets/uploads/` — photos uploaded in the dashboard
- `src/` — page templates, styles and scripts (`python3 src/build.py <out>`)
- `.github/workflows/build.yml` — rebuilds the pages after every change

See **BACKEND.md** for connecting forms to a server.
