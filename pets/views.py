from rest_framework import viewsets, permissions
from .serializers import TaskSerializer, TagSerializer  # Import TaskSerializer and TagSerializer
from .models import Task, Tag  # Import Task and Tag models

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]  # Adjust permissions as needed

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]  # Adjust permissions as needed
