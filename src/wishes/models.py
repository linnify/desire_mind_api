from django.db import models

from users.models import SwiftUser


def wishes_image_dir(instance, filename):
    return f"wishes/{instance.user.id}/{filename}"


class Wish(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(SwiftUser, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to=wishes_image_dir, max_length=255, null=True, blank=True)
