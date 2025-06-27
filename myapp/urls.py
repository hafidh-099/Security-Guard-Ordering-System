from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # CRUD Endpoints
    path('order/', views.manage_order),
    path('order/<int:pk>/', views.manage_order),
    
    path('organization/', views.manage_Organization),
    path('organization/<int:pk>/', views.manage_Organization),

    path('armedsecurityguard/', views.manage_ArmedSecurityGuard),
    path('armedsecurityguard/<int:pk>/', views.manage_ArmedSecurityGuard),

    path('securityoffice/', views.manage_SecurityOffice),
    path('securityoffice/<int:pk>/', views.manage_SecurityOffice),

    # Auth endpoints
    path('login/organization/', views.login_organization),
    path('login/securityoffice/', views.login_securityoffice),

    # 🔥 REGISTER endpoints
    path('register/organization/', views.register_organization),
    path('register/securityoffice/', views.register_securityoffice),  # ✅ THIS IS IMPORTANT
]
