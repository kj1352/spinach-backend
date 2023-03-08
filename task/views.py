from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from datetime import datetime, timedelta


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    from_date = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    to_date = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    queryset = Task.objects.filter(working_date__range=["2023-03-07", "2023-03-8"])
    serializer_class = TaskSerializer
