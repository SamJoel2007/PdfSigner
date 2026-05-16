# PDF Auto Signer

A simple Python utility for automatically stamping a signature image onto PDF files.

This project uses a small Tkinter GUI to trigger batch signing of PDFs stored in the `pdfs/` folder.

---

## Features

- Graphical launcher with basic actions
- Automatically signs all `.pdf` files inside the `pdfs/` directory
- Uses a configured image signature file and fixed position/size
- Saves signed PDFs with the same output filename

---

## Project structure

- `pdfsign.py` — main application script
- `pdfs/` — folder where source PDF files are stored
- `sign.jpeg` — default signature image used by the current configuration
- `sign1.pdf` — example or test PDF file
- `update_exe.py` — packaging helper script for building a standalone executable
- `update_exe.spec` — PyInstaller spec file generated during packaging
- `build/` — PyInstaller build artifacts
- `dist/` — generated standalone executable output

---

## Requirements

- Python 3.8+
- `PyMuPDF` (`fitz`)
- `pyhanko` (PDF signing helper library)
- `cryptography` (backend used by `pyhanko` for PKCS#12/key handling)
- `tkinter` (usually included with standard Python installations on Windows)
- `pyinstaller` (optional, only if building an executable)

Install required packages:

```bash
pip install pymupdf pyhanko cryptography pyinstaller
```

---

## Setup

1. Place the PDF files you want to sign inside the `pdfs/` directory.
2. Make sure the signature image is available and referenced by `signature_image` in `pdfsign.py`.
3. Optionally adjust these configuration values inside `pdfsign.py`:

```python
github_repo = ""
signature_image = "sign.jpeg"
X_POS = 100
Y_POS = 50
WIDTH = 200
HEIGHT = 80
page_num = -1
```

### Certificate (PFX) setup

The script expects a PKCS#12 file (PFX) named `my_identity.pfx` by default and a passphrase configured in `pdfsign.py`:

```python
pfx_file_name = "my_identity.pfx"
pfx_password = "root1234"
```

Place your `.pfx` file in the project root or update `pfx_file_name` to the correct path. The code encodes the passphrase automatically before calling `pyhanko`, so keep the passphrase as a normal string in the script.

- `X_POS`, `Y_POS` — signature position on the page
- `WIDTH`, `HEIGHT` — signature image dimensions
- `page_num` — target page index (`-1` = last page)

---

## Usage

Run the application from the project root:

```bash
python pdfsign.py
```

A window will appear with buttons:

- **Start Sign** — signs every PDF found in the `pdfs/` folder
- **How to Use?** — placeholder for usage instructions
- **Update Software** — placeholder for future update logic

### Packaging as an executable

To build a standalone executable using PyInstaller, run:

```bash
python update_exe.py
```

The generated executable and supporting files will appear in the `dist/` and `build/` folders.

---

## How it works

When you click **Start Sign**, the app:

1. scans `pdfs/` for PDF files
2. opens each PDF using `fitz`
3. inserts the signature image at the configured position
4. saves the output PDF using the same filename

---

## Notes

- `How to Use?` and `Update Software` are currently stubs and not fully implemented.
- The current script overwrites PDFs in place when signing.
- For production use, consider adding error handling, a preview screen, and separate output filenames.

---

## Future improvements

- Add an actual help screen inside the GUI
- Add a file picker for the signature image
- Add output filename control and backup handling
- Add support for multiple pages or custom page selection
