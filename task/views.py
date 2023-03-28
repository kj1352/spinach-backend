from .models import Task, Blocker
from .serializers import TaskSerializer,BlockerSerializer
from rest_framework import viewsets
from datetime import datetime, timedelta
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication], SessionAuthentication
    permission_classes = [IsAuthenticated]

class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    from_date = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    to_date = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    queryset = Task.objects.filter(working_date__range=[from_date, to_date])
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

class BlockerViewSet(viewsets.ModelViewSet):    
    queryset = Blocker.objects.all()
    serializer_class = BlockerSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

