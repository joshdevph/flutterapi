# Create your views here.
from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from todo_app import models
from .serializers import TodoSerializers

class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializers


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializers