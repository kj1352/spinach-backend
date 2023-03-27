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