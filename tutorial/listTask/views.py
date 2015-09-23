from .models import Task

from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    # serializer_class = TaskSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner = self.request.user)