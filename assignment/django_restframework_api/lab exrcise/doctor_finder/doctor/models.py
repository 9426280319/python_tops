from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ← add karo
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)

    def __str__(self):
        return self.name