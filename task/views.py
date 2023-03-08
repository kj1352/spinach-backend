from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer