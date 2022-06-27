from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from accounts.views import AdminViewSet, RegisterUserApiView, LoginView, AppointmentApiView

router = routers.DefaultRouter()
router.register(r'admin', AdminViewSet)



urlpatterns = [
    path('', include(router.urls)),
#    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/register/', RegisterUserApiView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/appointment/', AppointmentApiView.as_view(), name='appointment'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
