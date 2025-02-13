from django.db import models

class User(models.Model):
    face_encoding = models.BinaryField(null=True, blank=True)
    