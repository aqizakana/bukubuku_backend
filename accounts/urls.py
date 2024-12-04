from django.urls import path
from .views import UserRegistrationView, LoginView, LogoutView, UserDetailView, PasswordChangeView, UserInfoView

urlpatterns = [
  
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('password/change/', PasswordChangeView.as_view(), name='password-change'),
    path('userinfo/', UserInfoView.as_view(), name='user-info'),
]