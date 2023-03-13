from authentication.hashers import make_password, validate_password
from django.db import models
import uuid


class User(models.Model):
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = "email"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255, null=True, blank=True)
    is_superuser = None
    is_active = models.BooleanField(default=True)
    is_anonymous = None
    date_joined = models.DateField(auto_now_add=True)

    @property
    def is_authenticated(self):
        return True

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        return validate_password(password, self.password)
