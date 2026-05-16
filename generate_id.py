import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
# Explicitly import the pkcs12 module to prevent the AttributeError
from cryptography.hazmat.primitives.serialization import pkcs12

def create_self_signed_cert(pfx_path, password_str, country, org, sign, cert_name):
    # 1. Generate a private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # 2. Set up identity metadata
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, country),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, org),
        x509.NameAttribute(NameOID.COMMON_NAME, sign),
    ])

    # 3. Create the certificate (valid for 365 days)
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.now(datetime.timezone.utc)
    ).not_valid_after(
        datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365)
    ).add_extension(
        x509.KeyUsage(
            digital_signature=True,
            content_commitment=True,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=False,
            key_cert_sign=False,
            crl_sign=False,
            encipher_only=False,
            decipher_only=False
        ),
        critical=True
    ).sign(private_key, hashes.SHA256())

    # 4. Save everything together as a password-protected .pfx bundle
    # Note the change here: using pkcs12 directly instead of serialization.pkcs12
    pfx_data = pkcs12.serialize_key_and_certificates(
        name=cert_name.encode(),
        key=private_key,
        cert=cert,
        cas=None,
        encryption_algorithm=serialization.BestAvailableEncryption(password_str.encode())
    )

    with open(pfx_path, "wb") as f:
        f.write(pfx_data)
    print(f"Success! Testing certificate saved to: {pfx_path}")

# Run the generator

file_name = input("Enter pfx file name (e.g. MyIdentity): ")
file_name = file_name + ".pfx"
password = input("Enter password for the pfx file: ")
country = input("Enter country name (2-letter code, e.g. IN): ")
organization = input("Enter organization name (e.g. Test Organization): ")
signature = input("Type your signature here: ")
cert_name = input("Enter a name for the certificate (e.g. My Testing Certificate): ")

create_self_signed_cert(file_name, password, country, organization, signature, cert_name)
