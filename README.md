# Matan Shavit — Workshops Landing Page

Hebrew RTL landing-page mockup for Matan Shavit's acting and improvisation workshops for technology teams, managers, and organizations.

## Project structure

- `index.html` — current responsive mockup.
- `assets/images/reference/` — original reference photos supplied for visual development.
- `assets/images/generated/` — approved AI-generated workshop imagery.
- `docs/previews/` — static screenshots for quick review.

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

## Workflow

1. Approve copy, hierarchy, and layout in the HTML mockup.
2. Generate and approve workshop imagery featuring Matan.
3. Keep all source and generated imagery as local repository assets.
4. Publish the approved static site through GitHub Pages.

## Notes

- The page is designed RTL-first and responsive.
- Testimonials and company logos must only be published after verification and permission.
- All assets required by the public page are stored in this repository and use
  relative local paths.
