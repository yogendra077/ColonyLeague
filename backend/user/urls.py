"""
URL mappings for the user API.
"""
from django.urls import path

from user import views
from rest_framework import routers
from .views import UserViewset

router = routers.DefaultRouter()
router.register('', UserViewset)

urlpatterns = [
]
urlpatterns += router.urls
