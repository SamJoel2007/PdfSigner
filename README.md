<div align="center">

# 📝 PDF Auto Signer

**Automatically sign all your PDFs with a single click — powered by Python & pyhanko**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-latest-green?style=for-the-badge)
![pyhanko](https://img.shields.io/badge/pyhanko-latest-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-lightblue?style=for-the-badge&logo=windows)

</div>

---

## ✨ Features

- 🖱️ **Simple GUI** — Clean Tkinter window, no command line needed
- 📂 **Batch Signing** — Signs every PDF inside the `pdfs/` folder automatically
- 🔏 **Cryptographic Signature** — Uses a real PKCS#12 (.pfx) certificate via `pyhanko`
- 🖼️ **Image Stamp** — Overlays your signature image at a configurable position
- 📦 **Standalone EXE** — Can be packaged into a single `.exe` with PyInstaller
- 🔑 **Certificate Generator** — Includes `generate_id.py` to create your own `.pfx` file

---

## 📁 Project Structure

```
PdfSigner/
│
├── pdfs/                  # 👉 Drop your PDFs here to be signed
├── signed_pdf/            # 👉 Signed outputs appear here
│
├── pdfsign.py             # Main application
├── pdfsign.bat            # One-click launcher (installs deps + runs app)
├── generate_id.py         # Certificate (.pfx) generator
├── generate_id.bat        # One-click certificate generator
├── update_exe.py          # Builds standalone .exe via PyInstaller
│
├── MyIdentity.pfx         # Your signing certificate (do NOT share this)
├── sign.jpeg              # Your signature image
├── requirements.txt       # Python dependencies
└── README.md
```

---

## ⚙️ Configuration

Open `pdfsign.py` and edit the `CONFIG` section at the top:

```python
signature_image = "sign.jpeg"      # Your signature image file
pfx_file_name   = "MyIdentity.pfx" # Your certificate file
pfx_password    = "root1234"       # Your certificate password
page_num        = -1               # Page to sign (-1 = last page)
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

Or just double-click **`pdfsign.bat`** — it installs everything and launches the app.

### 2. Generate your signing certificate

If you don't have a `.pfx` file yet, run:

```bash
python generate_id.py
```

or double-click **`generate_id.bat`**. It will ask you:

```
Enter pfx file name (e.g. MyIdentity): MyIdentity
Enter password for the pfx file: ****
Enter country name (2-letter code, e.g. IN): IN
Enter organization name: My Company
Type your signature here: John Doe
Enter a name for the certificate: My Signing Cert
```

This generates `MyIdentity.pfx` in the project folder.

### 3. Add your PDFs

Drop all the PDF files you want signed into the **`pdfs/`** folder.

### 4. Run the app

```bash
python pdfsign.py
```

---

## 🖥️ GUI Overview

| Button | Action |
|---|---|
| **Start Sign** | Signs all PDFs in `pdfs/` and saves to `signed_pdf/` |
| **How to Use?** | Opens this README on GitHub |
| **Update Software** | Pulls the latest version from GitHub |

---

## 📦 Build as Standalone EXE

To package the app into a single `.exe`:

```bash
python update_exe.py
```

The output will be in the `dist/` folder. Share that `.exe` and it runs without Python installed.

---

## 🔐 Security Notes

> ⚠️ **Never share or commit your `.pfx` file to GitHub.**
> It contains your private key. Add it to `.gitignore`:

```
*.pfx
signed_pdf/
pdfs/
```

---

## 🛠️ Requirements

| Package | Purpose |
|---|---|
| `PyMuPDF` | PDF rendering and image stamping |
| `pyhanko` | Cryptographic PDF signing |
| `cryptography` | PKCS#12 / certificate handling |
| `tkinter` | GUI (bundled with Python on Windows) |
| `pyinstaller` | Building standalone executables |

---

## 🗺️ Roadmap

- [ ] File picker for signature image inside the GUI
- [ ] Preview before signing
- [ ] Custom output filename support
- [ ] Multi-page signing support
- [ ] Dark/light theme toggle

---

## 👨‍💻 Author

**SamJoel2007** — [GitHub](https://github.com/SamJoel2007)

---

<div align="center">
  Made with ❤️ and Python
</div>
