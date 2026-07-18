# Matan Shavit — Workshops Landing Page

Public Hebrew RTL landing-page mockup for Matan Shavit's acting and improvisation workshops for technology teams, managers, and organizations. The mockup is intended to communicate the concept and visual direction before a final website is built and approved.

## Project structure

- `index.html` — complete responsive website, including CSS and lightweight JavaScript.
- `assets/icons/` — local site icon.
- `assets/images/reference/` — optimized real photographs of Matan used by the public page.
- `assets/images/generated/` — AI-generated workshop scenes used to communicate the mockup's intended atmosphere.
- `docs/` — image-generation brief and earlier visual previews retained for the next design/content review.

## Local preview

Open `index.html` directly in a browser, or run a local server:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Live website

This repository is ready to be served by GitHub Pages from the `main` branch and
the repository root (`/`). After GitHub Pages is enabled, view the public site at:

https://tomeraminof.github.io/matan-workshops-site/

In the repository settings, select **Pages → Build and deployment → Deploy from
a branch**, then choose **main** and **/(root)**.

## Contact

The site links directly to WhatsApp at `+972 54-207-8475`. The contact form only composes a WhatsApp message in the visitor's browser; it does not collect or store submissions.

## Notes

- The page is designed RTL-first and responsive.
- Testimonials and company logos must only be published after verification and permission.
- Workshop-scene images are AI-generated mockup assets and are identified as such on the page. Review or replace them before publishing an official website.
- Real photographs of Matan remain in the about and stage sections to support authenticity.
- All assets required by the public page are stored in this repository and use
  relative local paths.
