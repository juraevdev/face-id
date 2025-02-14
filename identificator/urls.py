from django.urls import path
from .views import UserRegisterAPIView, UserUpdateAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user-create'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]
