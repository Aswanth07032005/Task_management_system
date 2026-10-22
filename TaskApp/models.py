from django.contrib.auth.models import AbstractUser
from django.db import models


class Register(AbstractUser):
    is_user = models.BooleanField(default=False)

    def __str__(self):
        return self.username




class UserRegister(models.Model):
    user = models.OneToOneField(
        Register,
        on_delete=models.CASCADE,
        related_name='user_profile'
    )
    name = models.CharField(max_length=250)
    email = models.EmailField()
    age = models.IntegerField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name





class Task(models.Model):
    user = models.ForeignKey(
        Register,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title