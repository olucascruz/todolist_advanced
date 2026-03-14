from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='categories')
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class Task(models.Model):
    class Meta:
        ordering = ['-created_at']
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    # Relacionamentos
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    
    # Compartilhamento: Permite que outros usuários vejam/editem
    # O campo corrigido abaixo:
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared_tasks', blank=True)

    def __str__(self):
        return self.title