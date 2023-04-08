"""
Views for the user API.
"""
from rest_framework import viewsets
from user.serializers import (
    UserSerializer,
)
from django.contrib.auth import (
    get_user_model,
)
from rest_framework import authentication, exceptions,response


class UserViewset(viewsets.ModelViewSet):
    queryset =  get_user_model().objects.all()
    serializer_class = UserSerializer
    
    def list(self,request):
        if  self.request.user.is_superuser is False:
            raise exceptions.PermissionDenied()
        users = get_user_model().objects.all()
        seriliazer =UserSerializer(users, many=True)
        return response.Response(seriliazer.data) 
