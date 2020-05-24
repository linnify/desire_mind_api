from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from rest_framework.response import Response

from wishes.models import Wish
from wishes.serializers import WishSerializer


class WishViewModel(viewsets.ModelViewSet):
    serializer_class = WishSerializer
    queryset = Wish.objects.all()
    permission_classes = ()
    parser_classes = (MultiPartParser,)

    @action(methods=["PUT"], detail=True, url_path="upload")
    def upload_image(self, request: Request, pk):
        try:
            wish = self.get_object()
        except Wish.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        file = request.FILES["file"]

        wish.image = file

        wish.save()

        return Response(status=status.HTTP_200_OK)
