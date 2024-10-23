from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FootballAreaViewSet

router = DefaultRouter()
router.register(r'areas', FootballAreaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
