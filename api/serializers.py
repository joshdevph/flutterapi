from rest_framework import serializers
from todo_app import models


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Todo