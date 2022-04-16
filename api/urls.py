from django.urls import path
from .views import GruposViewSet, UserViewSet
from rest_framework.routers import SimpleRouter


'''
urlpatterns = [
    path('', GruposViewSet.as_view(), name='home'),
]
'''


router = SimpleRouter()
router.register('grupos', GruposViewSet, basename='grupos')
router.register('', UserViewSet, basename='users')

urlpatterns = router.urls