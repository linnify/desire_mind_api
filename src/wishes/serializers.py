from rest_framework import serializers

from wishes.models import Wish
from helpers.fields import MinioFileField


class WishSerializer(serializers.ModelSerializer):
    image = MinioFileField(required=False)

    class Meta:
        model = Wish
        fields = ("id", "title", "description", "is_public", "user", "created_at", "modified_at", "image")
