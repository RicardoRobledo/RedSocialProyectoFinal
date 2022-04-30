from urllib.parse import urlparse
from django.urls import path, include
from .views import GruposViewSet, UserViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('grupos', GruposViewSet, basename='grupos')
router.register('', UserViewSet, basename='users')

urlpatterns = router.urls
