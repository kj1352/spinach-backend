from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='custom_users'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_users'
    )

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    user = models.CharField(max_length=25)
    working_date = models.DateField()

    def __str__(self):
        return self.user.name + ' - ' + self.title



class Blocker(models.Model):
    description = models.TextField(null=True, blank=True)
    user = models.CharField(max_length=25)
    working_date = models.DateField()

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.key
    
class Standup(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    yesterday = models.TextField()
    today = models.TextField()
    blockers = models.TextField(null=True, blank=True)