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

For Wix, choose the URL based on which navigation should remain visible:

- Keep the landing page's own menu: embed
  `https://tomeraminof.github.io/matan-workshops-site/` and enable the navigation
  bridge below.
- Use Wix's own menu and floating contact action: embed
  `https://tomeraminof.github.io/matan-workshops-site/?embed=1`.

Embed mode removes the landing page's own header, footer, and floating WhatsApp
button to avoid duplicating the surrounding Wix interface. The page remains
responsive, and the main WhatsApp actions open in a new tab.

### Wix navigation bridge

If the full landing page is embedded as one tall Wix iframe, its internal hash
links cannot scroll the outer Wix page by themselves. The site sends a secure
navigation message to `matanshavit.com` whenever an internal menu link is
selected.

Enable **Dev Mode / Velo** on the Wix page and add this page code, replacing
`#html1` with the ID of the **Embed a Site** element shown in the Wix editor:

```js
import wixWindowFrontend from 'wix-window-frontend';

const EMBED_ID = '#html1';
const WIX_HEADER_OFFSET = 80;

$w.onReady(() => {
  $w(EMBED_ID).onMessage(async (event) => {
    const message = event.data;
    if (message?.type !== 'matan-workshops:navigate') return;

    await $w(EMBED_ID).scrollTo();
    const viewport = await wixWindowFrontend.getBoundingRect();
    const targetY = Math.max(
      0,
      viewport.scroll.y + Number(message.offset || 0) - WIX_HEADER_OFFSET
    );

    await wixWindowFrontend.scrollTo(0, targetY, {
      scrollAnimation: true
    });
  });
});
```

An element inside an iframe cannot stay fixed to the outer Wix browser viewport.
For a truly floating WhatsApp action on the Wix page, add a Wix button (or the
Wix WhatsApp widget), pin it to the screen, and use the same `wa.me` URL from
this page.

## Contact

The site links directly to WhatsApp at `+972 54-207-8475`. The contact form only composes a WhatsApp message in the visitor's browser; it does not collect or store submissions.

## Notes

- The page is designed RTL-first and responsive.
- The landing page is organized into six focused sections: hero, workshop paths and capabilities, workshop experience and process, contact, about, and FAQ.
- Real photographs of Matan are used in the hero, about, and stage areas.
- All assets required by the public page are stored in this repository and use
  relative local paths.
