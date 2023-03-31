from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    working_date = models.DateField()

    def __str__(self):
        return self.user.name + ' - ' + self.title



class Blocker(models.Model):
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
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