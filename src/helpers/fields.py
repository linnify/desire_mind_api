from rest_framework import fields
from django.conf import settings
from urllib.parse import urlparse, ParseResult


class MinioFileField(fields.FileField):
    def to_representation(self, value):
        representation = super().to_representation(value)

        if not representation:
            return None

        parsed_url = urlparse(representation)

        adjusted_url = ParseResult(
            scheme=parsed_url.scheme,
            netloc=f"{parsed_url.hostname}:{settings.REVERSEPROXY_PORT}",
            path=parsed_url.path,
            params=parsed_url.params,
            query=parsed_url.query,
            fragment=parsed_url.fragment,
        )

        return adjusted_url.geturl()
