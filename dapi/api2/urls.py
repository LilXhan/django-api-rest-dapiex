from django.urls import path 
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('completed/', views.task_completed, name='completed')
]