from rest_framework import serializers
from .models import Task, Blocker, User, Standup,CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def create(self, validated_data):
        user = CustomUser(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
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