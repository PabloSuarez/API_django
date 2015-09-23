from django.conf.urls import include, url
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter


taskRouter = DefaultRouter()
taskRouter.register(r'listTask', TaskViewSet)

urlpatterns = [
    url(r'^', include(taskRouter.urls)),
]
