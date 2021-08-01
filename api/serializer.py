from rest_framework import serializers

from .models import User, Task

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("title", "detail", "deadline")