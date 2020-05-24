from django.contrib.auth.models import AbstractUser
from django.db import models


def user_profile_picture_dir(instance, filename):
    return f"users/{instance.id}/{filename}"


class SwiftUser(AbstractUser):
    profile_image = models.FileField(upload_to=user_profile_picture_dir, max_length=255, null=True, blank=True)
