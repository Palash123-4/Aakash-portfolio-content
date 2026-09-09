# Aakash Chowdhury — Research Portfolio

This repository contains the source files for **Aakash Chowdhury's academic research portfolio website**.

The website is generated from an XML content file using `generate_html.py`.

> **Important:** `index.html` is a generated file. When you want to change the website content, edit `portfolio-content.xml` and run `generate_html.py` again.

---

## 📁 Repository Structure

```text
Aakash-portfolio-content/
│
├── portfolio-content.xml   # Main source file for website content
├── generate_html.py        # Generates index.html from the XML file
├── index.html              # Generated website
├── assets/                 # Images, CV and other website assets
│   ├── aakash-lake.jpg
│   └── Aakash_Chowdhury_CV.pdf
│
└── README.md               # Documentation
```

---

## ⚙️ How the Website Works

The website follows this simple workflow:

```text
portfolio-content.xml
        │
        │  generate_html.py
        ▼
   index.html
        │
        ▼
   Web Browser
```

### Source of truth

`portfolio-content.xml` contains the editable website content, including:

- Personal introduction
- Navigation links
- Research areas
- Publications
- Projects
- Experience
- Contact information
- Website links
- Photo information

`generate_html.py` reads the XML file, generates the required HTML, CSS and JavaScript, and writes the result to:

```text
index.html
```

The Python script automatically looks for `portfolio-content.xml` in the same directory as the script. 

---

# 🐍 Running `generate_html.py`

## 1. Install Python

You need **Python 3**.

Check whether Python is installed:

### Linux / macOS

```bash
python3 --version
```

### Windows

```powershell
python --version
```

Python 3.8 or newer is recommended.

The generator uses Python's standard library, so **no external Python packages are required**.

---

## 2. Open the repository directory

Navigate to the directory containing:

```text
generate_html.py
portfolio-content.xml
```

For example:

```bash
cd Aakash-portfolio-content
```

---

## 3. Run the generator

### Linux / macOS

```bash
python3 generate_html.py
```

### Windows

```powershell
python generate_html.py
```

If the command completes successfully, `index.html` will be regenerated.

The script uses paths relative to its own directory, so it should normally be run directly from the repository directory or with its path specified.

---

# ✏️ Editing the Website

## Edit `portfolio-content.xml`

For normal content changes, edit:

```text
portfolio-content.xml
```

Do **not** manually edit the generated `index.html` for content changes.

After modifying the XML file, run:

```bash
python3 generate_html.py
```

Then refresh the website.

### Recommended workflow

```text
1. Edit portfolio-content.xml
          ↓
2. Run generate_html.py
          ↓
3. Check index.html
          ↓
4. Test the website locally
          ↓
5. Commit the changes
          ↓
6. Push to GitHub
```

---

# 🎨 Changing the Website Design

The visual styling is defined inside:

```text
generate_html.py
```

The generator contains the CSS used by the website.

Therefore, if you want to change:

- Colours
- Fonts
- Typography
- Spacing
- Layout
- Responsive behaviour
- Buttons
- Cards
- Navigation
- Sections

edit the corresponding CSS in:

```text
generate_html.py
```

Then regenerate the website:

```bash
python3 generate_html.py
```

### Important

If you edit the generated `index.html` directly, your changes may be overwritten the next time you run:

```bash
python3 generate_html.py
```

So permanent design changes should be made in `generate_html.py`.

---

# 🖼️ Images and Other Assets

Website assets are stored in:

```text
assets/
```

For example:

```text
assets/aakash-lake.jpg
```

The generated website references these files using relative paths.

Therefore, keep the `assets` directory in the repository.

If you replace the profile/hero image, keep the expected filename:

```text
assets/aakash-lake.jpg
```

or update the corresponding image path in:

```text
portfolio-content.xml
```

After changing the image path, regenerate the website:

```bash
python3 generate_html.py
```

---

# 📄 CV

The downloadable CV is stored in:

```text
assets/Aakash_Chowdhury_CV.pdf
```

To update the CV:

1. Replace the existing PDF with the new version.
2. Keep the same filename:

```text
Aakash_Chowdhury_CV.pdf
```

3. Regenerate the website if necessary.
4. Check that the CV link works in the generated website.

---

# 🌐 Preview the Website Locally

You can open `index.html` directly in a browser.

However, using a small local HTTP server is recommended because it more closely resembles how the website behaves when hosted online.

From the repository directory, run:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

On Windows:

```powershell
python -m http.server 8000
```

Then open the same address in your browser.

Press:

```text
Ctrl + C
```

in the terminal to stop the server.

---

# 🔄 Recommended Development Workflow

Whenever you make changes to the portfolio, use:

```bash
# 1. Edit the source content
nano portfolio-content.xml
```

or open the file in VS Code:

```bash
code portfolio-content.xml
```

Then regenerate:

```bash
python3 generate_html.py
```

Start the local server:

```bash
python3 -m http.server 8000
```

Open:

```text
http://localhost:8000
```

Check the website.

If everything looks correct:

```bash
git status
git add .
git commit -m "Update portfolio"
git push
```

---

# 🚀 Publishing with GitHub Pages

This repository can be used as the source for a GitHub Pages website.

After generating `index.html`, make sure the repository contains:

```text
index.html
portfolio-content.xml
generate_html.py
assets/
```

Then configure GitHub Pages:

1. Open the repository on GitHub.
2. Go to **Settings**.
3. Select **Pages**.
4. Under **Build and deployment**, select:
   - **Source:** Deploy from a branch
   - **Branch:** `main`
   - **Folder:** `/ (root)`
5. Click **Save**.

GitHub will provide the published website URL.

---

# 🔁 Updating the Live Website

A typical update should look like this:

```bash
git pull
```

Edit the content:

```text
portfolio-content.xml
```

Generate the website:

```bash
python3 generate_html.py
```

Test locally:

```bash
python3 -m http.server 8000
```

Then commit and push:

```bash
git add .
git commit -m "Update research portfolio"
git push
```

GitHub Pages will then update the deployed website.

---

# 🛠️ Troubleshooting

## `python3: command not found`

Python 3 is not installed or is not available in your PATH.

Check:

```bash
python3 --version
```

or:

```bash
python --version
```

Install Python 3 if necessary.

---

## `FileNotFoundError: portfolio-content.xml`

Make sure `portfolio-content.xml` is in the same directory as:

```text
generate_html.py
```

The generator determines its directory automatically and looks for the XML file there. 

---

## The website did not change after editing the XML

Make sure you regenerated the HTML:

```bash
python3 generate_html.py
```

Then refresh your browser.

A hard refresh may also be useful:

```text
Ctrl + Shift + R
```

---

## The image is missing

Check that the image exists:

```text
assets/aakash-lake.jpg
```

Also check that the image path specified in `portfolio-content.xml` matches the actual filename.

Remember that Linux is case-sensitive:

```text
aakash-lake.jpg
```

is different from:

```text
Aakash-Lake.jpg
```

---

## Changes to `index.html` disappeared

This is expected if you manually edited `index.html` and subsequently ran:

```bash
python3 generate_html.py
```

`index.html` is generated by the Python script.

Make permanent changes in:

```text
portfolio-content.xml
```

for content, or:

```text
generate_html.py
```

for the website's design/generation logic.

Then regenerate:

```bash
python3 generate_html.py
```

---

# 📌 Quick Reference

| Task | Command / File |
|---|---|
| Edit website content | `portfolio-content.xml` |
| Change website design | `generate_html.py` |
| Generate website | `python3 generate_html.py` |
| Generated website | `index.html` |
| Website assets | `assets/` |
| Local preview | `python3 -m http.server 8000` |
| Local URL | `http://localhost:8000` |
| Publish | GitHub Pages |
| Update website | Edit → Generate → Test → Commit → Push |

---

## ⭐ In Short

If you only remember one thing, use this workflow:

```bash
# Edit the content
# portfolio-content.xml

# Generate the website
python3 generate_html.py

# Test locally
python3 -m http.server 8000

# Commit and publish
git add .
git commit -m "Update portfolio"
git push
```

**`portfolio-content.xml` → `generate_html.py` → `index.html` → GitHub Pages**