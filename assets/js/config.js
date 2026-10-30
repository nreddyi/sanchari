/* Sanchari site settings.
   Backend: put your API address in `base` (no trailing slash) and every form
   (enquiry, newsletter, booking, signup, login, profile) is POSTed there as JSON.
   Leave it empty to keep the site browser-only. See BACKEND.md. */
window.SANCHARI_API = {
  base: "",            // e.g. "https://api.sanchari.travel"
  headers: {},         // e.g. { "X-Api-Key": "public-site-key" }
  credentials: "omit"  // use "include" if your API sets login cookies
};
