from rest_framework import serializers
from .models import Task, Blocker


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'user', 'working_date']


class BlockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blocker
        fields = '__all__'