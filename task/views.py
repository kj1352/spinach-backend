from .models import Task, Blocker,Standup
from .serializers import TaskSerializer,BlockerSerializer,StandupSerializer
from rest_framework import viewsets
from datetime import datetime, timedelta
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    from_date = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    to_date = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    queryset = Task.objects.filter(working_date__range=[from_date, to_date])
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class BlockerViewSet(viewsets.ModelViewSet):    
    queryset = Blocker.objects.all()
    serializer_class = BlockerSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

class LoginView(ObtainAuthToken):
    authentication_classes = (TokenAuthentication)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username})
    
class SomeAuthenticatedView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user
        # Do something with the authenticated user
        return Response({'message': f'Hello, {user.username}!'})    
    
class StandupViewSet(viewsets.ModelViewSet):
    serializer_class = StandupSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Standup.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    