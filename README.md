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

## Workflow

1. Approve copy, hierarchy, and layout in the HTML mockup.
2. Generate and approve workshop imagery featuring Matan.
3. Keep all source and generated imagery as local repository assets.
4. Rebuild the approved design in Wix section by section.

## Notes

- The page is designed RTL-first and responsive.
- Testimonials and company logos must only be published after verification and permission.
- Reference photos are stored for design use and should not be published automatically.

## Local reference photos

The site expects six source photos under `assets/images/reference/` and does not rely on Wix URLs after they are downloaded.

```bash
python scripts/download_reference_images.py
```

The source mapping is stored in `assets/images/reference/manifest.json`. These photos are source/reference assets; generated workshop scenes belong in `assets/images/generated/`.

## GitHub image sync

On the first push to `main`, GitHub Actions downloads the six Wix source photos into `assets/images/reference/` and commits them back to the repository. The workflow can also be run manually from the Actions tab.
