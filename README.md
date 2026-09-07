# Aakash Chowdhury — Research Portfolio

This is a static personal academic website. It has **no compilation, install, or build step**.

## Open it locally

1. Keep the `assets` folder beside `index.html`.
2. Double-click `index.html`, or right-click it and choose a browser.
3. The site opens locally. Internet access is only needed for the optional Google web fonts; readable system-font fallbacks are built in.

The photo is stored as `assets/aakash-lake.jpg` and loaded by `./assets/aakash-lake.jpg`. If it is moved or missing, the page displays a visible fallback message instead of a broken image.

## Edit it

Use any plain-text editor (for example VS Code or Notepad):

- `index.html` — the words, sections, links, and page structure.
- `styles.css` — colours, typography, spacing, and responsive design.
- `script.js` — mobile menu, current year, and the photo fallback.
- `assets/Aakash_Chowdhury_CV.pdf` — the downloadable CV.

After saving, refresh the browser. Do not rename `assets/aakash-lake.jpg` unless you also update the corresponding image path in `index.html`.

## Publish with GitHub Pages

1. Create a new GitHub repository, for example `aakash-chowdhury.github.io` (for a user site) or any name (for a project site).
2. Upload the *contents* of this folder: `index.html`, `styles.css`, `script.js`, `README.md`, and the complete `assets` folder.
3. On GitHub, open **Settings → Pages**.
4. Under **Build and deployment**, select **Deploy from a branch**, choose `main` and `/ (root)`, then save.
5. Wait a minute or two, then open the URL GitHub shows. A user-site repository normally appears at `https://YOUR-USERNAME.github.io/`; a project repository normally appears at `https://YOUR-USERNAME.github.io/REPOSITORY-NAME/`.

Because every file uses relative paths (`./styles.css` and `./assets/...`), the site works both locally and from a GitHub Pages project subfolder.
