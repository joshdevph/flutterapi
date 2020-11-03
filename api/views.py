from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from todo_app.models import Todo
from .serializers import TodoSerializers

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers