from django.conf.urls import include, url
from .views import TaskViewSet, news
from rest_framework.routers import DefaultRouter


taskRouter = DefaultRouter()
taskRouter.register(r'^listTask', TaskViewSet)

urlpatterns = [
    url(r'^listTask/news', news),
    url('', include(taskRouter.urls)),
]
