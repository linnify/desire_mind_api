from django.urls import path
from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from users import views


router = routers.DefaultRouter(trailing_slash=False)
router.register("users", views.SwiftUserModelViewSet, base_name="users")

urlpatterns = [
    path("profile", views.user_profile),
    url(r"^", include(router.urls)),
]
