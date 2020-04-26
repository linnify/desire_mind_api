from rest_framework import viewsets

from wishes.models import Wish
from wishes.serializers import WishSerializer


class WishViewModel(viewsets.ModelViewSet):
    serializer_class = WishSerializer
    queryset = Wish.objects.all()
