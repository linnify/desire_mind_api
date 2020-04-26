from django.contrib.auth.models import User
from django.db import models


class Wish(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
