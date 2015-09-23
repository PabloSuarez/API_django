from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.utils import timezone

import datetime
now = datetime.date.today()

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(owner = self.request.user)


@api_view(['GET'])
def news(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
