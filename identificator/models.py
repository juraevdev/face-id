from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    face_encoding = models.BinaryField(null=True, blank=True)
    