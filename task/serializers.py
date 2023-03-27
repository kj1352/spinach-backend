from rest_framework import serializers
from .models import Task, Blockers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'user', 'working_date']


class BlockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blockers
        fields = '__all__'