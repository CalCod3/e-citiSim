import imp
from django.contrib.auth.models import User, Group
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class= UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class= GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class RegisterUserApiView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer