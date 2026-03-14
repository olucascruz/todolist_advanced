from rest_framework import serializers
from .models import Task, Category
from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    # O owner é preenchido automaticamente pelo sistema, então deixamos como read_only
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner']

class TaskSerializer(serializers.ModelSerializer):
    # Mostra os detalhes do dono e da categoria (Read Only para facilitar o GET)
    owner = UserSerializer(read_only=True)
    shared_with_details = UserSerializer(many=True, read_only=True, source='shared_with')
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'created_at', 
            'due_date', 'completed', 'category', 'owner', 
            'shared_with', 'shared_with_details'
        ]