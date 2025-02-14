from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    face_encoding = ArrayField(models.FloatField(), null=True, blank=True)
    