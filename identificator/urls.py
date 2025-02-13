from django.urls import path
from .views import UserCreateAPIView, UserUpdateAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-create'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
]
