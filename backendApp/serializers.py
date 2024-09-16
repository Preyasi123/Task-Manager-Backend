from rest_framework import serializers
from backendApp.models import Todo

class Todo_serializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        read_only_fields = ["id"]
