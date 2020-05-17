from rest_framework import serializers

from helpers.fields import MinioFileField
from users.models import SwiftUser


class SwiftUserSerializer(serializers.ModelSerializer):
    profile_image = MinioFileField(required=False)

    class Meta:
        model = SwiftUser
        fields = ("id", "email", "first_name", "last_name", "profile_image", "password")
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = SwiftUser(**validated_data)
        user.set_password(password)

        user.save()

        return user
