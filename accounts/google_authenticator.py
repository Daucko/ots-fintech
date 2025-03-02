import pyotp # type: ignore
import qrcode

def generate_qr_code(user):
    secret_key = pyotp.random_base32()
    totp = pyotp.TOTP(secret_key)
    uri = totp.provisioning_uri(user.email, issuer_name="YourAppName")

    qr = qrcode.make(uri)
    with open(f"{user.username}_qrcode.png", "wb") as f:
        qr.save(f)

    return secret_key  
