from django.shortcuts import render
from rest_framework import viewsets
from backendApp.models import Todo
from backendApp.serializers import Todo_serializer
# Create your views here.
class TodoViewset(viewsets.ModelViewSet):
    serializer_class = Todo_serializer
    queryset = Todo.objects.all()
    model = Todo