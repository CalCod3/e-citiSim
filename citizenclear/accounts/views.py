import imp
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from rest_framework import permissions
from .models import CustomUser, Appointment
from .serializers import AppointmentSerializer, UserSerializer, RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class= UserSerializer
    permission_classes = [permissions.IsAuthenticated]

#class GroupViewSet(viewsets.ModelViewSet):
#    queryset = Group.objects.all()
#    serializer_class= GroupSerializer
#    permission_classes = [permissions.IsAuthenticated]
    
class RegisterUserApiView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class= AppointmentSerializer
    permission_classes = [permissions.IsAdminUser]
