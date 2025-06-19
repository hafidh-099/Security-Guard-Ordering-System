from django.contrib import admin
from django.urls import path, include  # include is very important!



from django.urls import path
from myapp import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # JWT authentication URLs
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API views
    path('order/', views.manage_order),
    path('order/<int:pk>/', views.manage_order),

    path('organization/', views.manage_Organization),
    path('organization/<int:pk>/', views.manage_Organization),

    path('armedsecurityguard/', views.manage_ArmedSecurityGuard),
    path('armedsecurityguard/<int:pk>/', views.manage_ArmedSecurityGuard),

    path('securityoffice/', views.manage_SecurityOffice),
    path('securityoffice/<int:pk>/', views.manage_SecurityOffice),
]
