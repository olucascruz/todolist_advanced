from rest_framework import viewsets, permissions
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters # Para busca por texto

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # O usuário só vê as categorias que ele mesmo criou
        return Category.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Define automaticamente o dono da categoria como o usuário logado
        serializer.save(owner=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # Adicionamos os backends de filtro e busca
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Quais campos podem ser filtrados exatamente
    filterset_fields = ['completed', 'category'] 
    
    # Quais campos podem ser buscados por texto
    search_fields = ['title', 'description']

    def get_queryset(self):
        user = self.request.user
        # Lógica avançada: Tarefas que eu sou dono OU que foram compartilhadas comigo
        return Task.objects.filter(Q(owner=user) | Q(shared_with=user)).distinct()

    def perform_create(self, serializer):
        # Define o dono da tarefa como o usuário logado no momento da criação
        serializer.save(owner=self.request.user)