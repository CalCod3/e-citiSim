from rest_framework.response import  Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from rest_framework import status
from .utils import get_tokens_for_user
from .models import CustomUser, Appointment
from .serializers import AppointmentSerializer, RegisterSerializer
#from rest_framework.decorators import authentication_classes

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = CustomUser.objects.all()
#    serializer_class= UserSerializer
#    permission_classes = [permissions.IsAuthenticated]

#class GroupViewSet(viewsets.ModelViewSet):
#    queryset = Group.objects.all()
#    serializer_class= GroupSerializer
#    permission_classes = [permissions.IsAuthenticated]
    
class RegisterUserApiView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class AppointmentApiView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class= AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class= AppointmentSerializer
    permission_classes = [permissions.IsAdminUser]


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
#    @authentication_classes([JSONWebTokenAuthentication])
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'You have entered Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

      
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


      
