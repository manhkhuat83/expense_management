import pyotp


def generate_otp():
    global otp
    secret = pyotp.random_base32()
    otp = pyotp.TOTP(secret, interval=300)
    one_time = otp.now()
    return one_time


def verify_otp(one_time):
    return bool(otp.verify(one_time))
