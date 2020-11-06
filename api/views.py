# Create your views here.
from todo_app.models import Todo
from .serializers import TodoSerializers

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'List':'/task-list/',
        'Detail View' : '/task-detail/'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Todo.objects.all().order_by('-id')
    serializer = TodoSerializers(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Todo.objects.get(id=pk)
    serializer = TodoSerializers(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TodoSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Todo.objects.get(id=pk)
    serializer = TodoSerializers(instance=tasks, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Todo.objects.get(id=pk)
    tasks.delete()
    return Response()
