from django.conf import settings
import base64
import hashlib
import bcrypt


def make_password(password, encoder=settings.DEFAULT_ENCODING):
    return bcrypt.hashpw(
        base64.b64encode(hashlib.sha256(password.encode(encoder)).digest()),
        bcrypt.gensalt(),
    ).decode(encoder)


def validate_password(password, hashed, encoder=settings.DEFAULT_ENCODING):
    return bcrypt.checkpw(
        base64.b64encode(hashlib.sha256(password.encode(encoder)).digest()),
        hashed.encode(encoder),
    )
