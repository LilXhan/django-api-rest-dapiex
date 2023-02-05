from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Task
from .serializer import TaskSerializer

@api_view(['GET', 'POST'])
def tasks(request):

    if request.method == 'GET':
        tasks = Task.objects.all()

        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def task_completed(request):

    if request.method == 'PUT':
        task = Task.objects.get(pk=request.data['id'])

        if task is not None:
            task.finished()

            serializer = TaskSerializer(task)

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)