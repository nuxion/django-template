from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .managers import EmailUserManager


## comment out if you want to use a thin wrapper around
## user default model
# class CustomUser(AbstractUser):
#     # add additional fields in here
#     # test_name = models.CharField(max_length=30, default=None, null=True)
#     def __str__(self):
#         return self.username
# 
#     class Meta:
#         managed = False


class OwnedModel(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE
    )
    owner_group = models.ForeignKey("auth.Group", null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class EmailUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = EmailUserManager()
