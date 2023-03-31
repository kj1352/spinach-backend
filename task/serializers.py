from rest_framework import serializers
from .models import Task, Blocker, User, Standup


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'user', 'working_date']


class BlockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blocker
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class StandupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standup
        fields = ('id', 'user', 'date', 'yesterday', 'today', 'blockers')
        read_only_fields = ('id', 'date', 'user')    