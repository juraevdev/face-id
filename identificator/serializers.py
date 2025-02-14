from rest_framework import serializers
from .models import User
import json

class UserSerializer(serializers.ModelSerializer):
    face_encoding = serializers.JSONField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'face_encoding']
