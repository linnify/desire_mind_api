import datetime
import typing as T
from urllib.parse import urlparse

from minio_storage.storage import MinioMediaStorage


class CustomMinioMediaStorage(MinioMediaStorage):

    def url(
        self, name: str, *args, max_age: T.Optional[datetime.timedelta] = None
    ):
        original_url = super().url(name=name, *args, max_age=max_age)
        parsed_url = urlparse(original_url)
        return f"{parsed_url.path}?{parsed_url.params}{parsed_url.query}{parsed_url.fragment}"
