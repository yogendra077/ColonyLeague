"""
Views for the teams API.
"""
from rest_framework import viewsets
# from ..core import models
from rest_framework import permissions,authentication, exceptions,response
from .serializers import TeamSerializer
from core import models

class TeamViewset(viewsets.ModelViewSet):
    queryset =  models.Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAdminUser]
    
