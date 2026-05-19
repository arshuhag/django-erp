from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    MeAPIView,
    AdminDashboardAPIView,
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),

    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    path('me/', MeAPIView.as_view(), name='me'),

    path(
        'admin/dashboard/',
        AdminDashboardAPIView.as_view(),
        name='admin-dashboard'
    ),
]