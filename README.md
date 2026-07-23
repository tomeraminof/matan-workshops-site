# Matan Shavit — Workshops Landing Page

Production-ready Hebrew RTL landing page for Matan Shavit's acting and improvisation workshops for technology teams, managers, and organizations.

## Project structure

- `index.html` — complete responsive website, including CSS and lightweight JavaScript.
- `assets/icons/` — local site icon.
- `assets/images/reference/` — optimized real photographs of Matan used by the public page.
- `assets/images/generated/` — workshop imagery used by the public page.
- `docs/` — internal visual-development materials that are not loaded by the website.

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

For Wix, use the dedicated embed URL in an **Embed a Site** element:

https://tomeraminof.github.io/matan-workshops-site/?embed=1

Embed mode removes the landing page's own header, footer, and floating WhatsApp
button to avoid duplicating the surrounding Wix interface. The page remains
responsive, and the main WhatsApp actions open in a new tab.

## Contact

The site links directly to WhatsApp at `+972 54-207-8475`. The contact form only composes a WhatsApp message in the visitor's browser; it does not collect or store submissions.

## Notes

- The page is designed RTL-first and responsive.
- The landing page is organized into six focused sections: hero, workshop paths and capabilities, workshop experience and process, contact, about, and FAQ.
- Real photographs of Matan are used in the hero, about, and stage areas.
- All assets required by the public page are stored in this repository and use
  relative local paths.
