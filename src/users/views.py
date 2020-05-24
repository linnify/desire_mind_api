from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins

from users.models import SwiftUser
from users.serializers import SwiftUserSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_profile(request):
    try:
        user = request.user

        context = {"request": request}
        serializer = SwiftUserSerializer(user, context=context)

        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND)


class SwiftUserModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SwiftUserSerializer
    permission_classes = ()
    queryset = SwiftUser.objects.all()

    @action(methods=["POST"], detail=True, url_path="/profile-picture")
    def upload_profile_picture(self, request, pk):
        try:
            user: SwiftUser = self.get_object()
        except SwiftUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        file = request.FILES["file"]

        user.profile_image = file

        user.save()

        return Response(status=status.HTTP_200_OK)
