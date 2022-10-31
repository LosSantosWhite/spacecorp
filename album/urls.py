from rest_framework import routers

from django.urls import path, include
from album.api.v1.api import AlbumViewSet

router = routers.DefaultRouter()
router.register("v1/albums", AlbumViewSet)

urlpatterns = router.urls
