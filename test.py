from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import signers, fields
from pyhanko.stamp import TextStampStyle  # ← correct location

# 1. Load PFX certificate
cms_signer = signers.SimpleSigner.load_pkcs12(
    pfx_file="my_identity.pfx", passphrase=b"root1234"
)

# 2. Open PDF and append empty signature field
with open("pdfs/1.pdf", 'rb') as inf:
    w = IncrementalPdfFileWriter(inf, strict=False)
    fields.append_signature_field(
        w, sig_field_spec=fields.SigFieldSpec(
            sig_field_name='Sig1', on_page=-1, box=(100, 100, 300, 150)
        )
    )
    
    # 3. Define signature appearance and sign
    custom_stamp = TextStampStyle(  # ← no more stamp.TextStampStyle
    stamp_text="Signed by: %(signer)s\nDate: %(ts)s"
    )
    pdf_signer = signers.PdfSigner(
        signature_meta=signers.PdfSignatureMetadata(field_name='Sig1'),
        signer=cms_signer, stamp_style=custom_stamp
    )
    
    with open("output.pdf", 'wb') as outf:
        pdf_signer.sign_pdf(w, output=outf)
