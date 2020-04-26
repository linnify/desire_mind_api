from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register("wishes", views.Wish, base_name='wishes')

urlpatterns = [url(r"^", include(router.urls))]
