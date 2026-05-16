from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import signers, fields
from pyhanko.stamp import TextStampStyle 
import tkinter as tk
import subprocess
import fitz
import os
import re

# CONFIG

github_repo = "https://github.com/SamJoel2007/PdfSigner.git"
github_repo_READMEmd = "https://github.com/SamJoel2007/PdfSigner/blob/master/README.md"

signature_image = "sign.jpeg"
pfx_file_name = "MyIdentity.pfx"
pfx_password = "root1234"
page_num = -1 # LAST PAGE

# END OF CONFIG

class pdfsigner:
    def app():

        root = tk.Tk()
        root.title("PDF AUTO SIGNER")
        root.geometry("500x500")
        root.config(bg="#1e1e1e")

        tk.Label(root, text="PDF AUTO SIGNER", font=("Arial", 24), bg="#1e1e1e", fg="white").pack(pady=20)

        tk.Button(root, text="Start Sign",  command=lambda: pdfsigner.main("start"),  width=20, height=2, font=("Arial", 12)).pack(pady=5)
        tk.Button(root, text="How to Use?", command=lambda: pdfsigner.main("howto"), width=20, height=2, font=("Arial", 12)).pack(pady=5)
        tk.Button(root, text="Update Software", command=lambda: pdfsigner.main("update"), width=20, height=2, font=("Arial", 12)).pack(pady=5)
        root.mainloop()

    @staticmethod
    def attach_signature(input_pdf, signature_img, output_pdf):
        print("STARTING SIGNING PROCESS...")
        # 1. Load PFX certificate
        try:
            passphrase_bytes = pfx_password.encode('utf-8') if pfx_password is not None else None
            cms_signer = signers.SimpleSigner.load_pkcs12(
                pfx_file=pfx_file_name, passphrase=passphrase_bytes
            )
        except Exception as e:
            print("Could not load key material from PKCS#12 file:", e)
            try:
                pdfsigner.message('Could not load key material from PKCS#12 file. Check console.')
            except Exception:
                pass
            return

        input_pdf = "pdfs/" + input_pdf

        with open(input_pdf, 'rb') as inf:
            w = IncrementalPdfFileWriter(inf, strict=False)
            fields.append_signature_field(
            w, sig_field_spec=fields.SigFieldSpec(
            sig_field_name='Sig1', on_page=page_num, box=(100, 100, 300, 150)
        )
        )

            custom_stamp = TextStampStyle( 
            stamp_text="Signed by: %(signer)s\nDate: %(ts)s"
            )

            pdf_signer = signers.PdfSigner(
            signature_meta=signers.PdfSignatureMetadata(field_name='Sig1'),
            signer=cms_signer, stamp_style=custom_stamp
            )

            output_pdf = "signed_pdf/" + output_pdf
            with open(output_pdf, 'wb') as outf:
                pdf_signer.sign_pdf(w, output=outf)

    def update_software():
        command = "git clone " + github_repo
        subprocess.run(command, shell=True)

    def how_to_use():
        command = "start " + github_repo_READMEmd
        subprocess.run(command, shell=True)

    def message(text):
        text = text.replace('"', "'")
        command = 'echo x=msgbox("{}", 0, "Notification") > %TEMP%\\msg.vbs && cscript //nologo %TEMP%\\msg.vbs && del %TEMP%\\msg.vbs'.format(text)
        subprocess.run(command, shell=True)
        return

    def main(op):
        if op == "start":
            # GET ALL THE PDF FILES INSIDE pdfs dir
            pdf_files = subprocess.run("dir pdfs", shell=True, capture_output=True, text=True)
            pdf_files = re.findall(r'\S+\.pdf', str(pdf_files.stdout))
            for pdf in pdf_files:
                pdfsigner.attach_signature(pdf, signature_image, pdf)
        elif op == "update":
            pdfsigner.update_software()
        elif op == "howto":
            pdfsigner.how_to_use()
        else:
            print("Invalid option")

if __name__ == "__main__":
    pdfsigner.app()