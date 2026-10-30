# Sanchari website — backend handoff

The site is static HTML (built by `src/build.py`, hosted on GitHub Pages). Everything a
visitor submits currently stays in their browser. This file lists what a backend needs to
take over.

## 1. Connect the forms (one setting)

Edit `src/config.js` (published as `assets/js/config.js`):

```js
window.SANCHARI_API = { base: "https://api.sanchari.travel", headers: {}, credentials: "omit" };
```

With `base` set, every form is POSTed as JSON to `{base}/{form}` (`Content-Type: application/json`,
`keepalive: true`). The site keeps its current on-page behaviour, so the backend only needs
to accept and store. Your API must allow CORS from the site's domain (`OPTIONS` preflight +
`Access-Control-Allow-Origin`). Every payload also contains `page` and `submitted_at` (ISO time).

| Endpoint | Form (id / `data-form`) | Where | Fields (`name`) |
|---|---|---|---|
| `POST /enquiry` | `#enquiryForm` / `enquiry` | Home, About, Contact, every tour & listing page | `trip_type` (temple, adventure, wellness, custom, general), `name`*, `phone`*, `email` (* required for general), `tour`, `travel_month` (YYYY-MM), `travellers`, `budget`, `message` |
| `POST /newsletter` | `#nlForm` / `newsletter` | Every page (above footer) | `email` |
| `POST /booking` | `#bookForm` / `booking` | Every tour page | `travel_style` (individual, group), `travel_date` (YYYY-MM-DD), `name`, `phone`, `email`, `invoice_no`, `tour` (slug), `adults`, `children`, `price_per_person`, `total` |
| `POST /signup` | `#pane-signup` / `signup` | Login pop-up | `name`, `phone`, `email`, `password`, `password_confirm`, `accept_terms` (bool) |
| `POST /login` | `#pane-login` / `login` | Login pop-up | `email` (email **or** phone), `password`, `remember` (bool) |
| `POST /profile` | `#acProfile` / `profile` | My Account → Profile | `name`, `phone`, `email`, `city`, `notes` |

Search forms (`#homeSearch`, `#searchForm`) only filter on the page and don't need an API:
`activity`, `destination`, `travel_month`, `duration`, `travel_style`, `max_budget`.

## 2. Replace the browser-only parts

| Today (browser only) | Backend should provide |
|---|---|
| Login/sign-up just remember the name in `localStorage` (`san_user`); no password check | Real accounts: hash passwords, sessions or tokens, password reset (the "Forgot password?" link currently only shows a message) |
| Bookings saved in `localStorage` (`san_bookings`), shown in My Account | Store bookings; `GET /me/bookings` for My Account |
| Wishlist in `localStorage` (`san_wishlist`) | Optional: `GET/POST /me/wishlist` |
| Invoice number made in the browser (`SAN-YYYYMMDD-NNNN`, random) | Issue sequential invoice numbers server-side (GST rules) |
| Invoice page builds itself from the URL (`invoice.html?tour=…&date=…&a=…&c=…&style=…&name=…&inv=…`) | Generate invoices from stored bookings; send by email |
| GST 5% and business details (GSTIN, PAN, bank, UPI) are placeholders in `src/build.py` (`TAX`, `BIZ`) | Confirm rate and details |
| No payments | Payment gateway (e.g. Razorpay) on the booking step |

The browser store lives in `window.SAN` at the top of `src/site.js`
(`user()`, `setUser()`, `bookings()`, `addBooking()`, `wishlist()`, `toggleWish()`), which is the single place to swap for API calls.

## 3. Content

* Tours: `content/tours/*.json` (edited in the Pages CMS dashboard). Fields are listed in `.pages.yml`.
  A backend can read the same JSON to validate tour slugs and prices on booking (never trust the price sent from the browser).
* Photos: `assets/photos/` (downloaded), `assets/uploads/` (dashboard uploads).
* Build: `python3 src/build.py <out-folder>`; GitHub Action `.github/workflows/build.yml` rebuilds on every change.
  Set `SITE_URL` env var when moving to the real domain (canonical links, sitemap, share previews).

## 4. Still to provide

Social profile URLs (`SOCIAL_URLS` in `src/build.py`), real prices/itineraries confirmation,
final policy texts, Anmish Varma photo.
