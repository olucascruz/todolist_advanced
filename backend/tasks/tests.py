import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
class TestTaskAPI:
    def test_list_tasks_only_returns_owned_or_shared(self, api_client, django_user_model):
        # --- ARRANGE ---
        # Adicionamos e-mails únicos para evitar o IntegrityError
        user1 = django_user_model.objects.create_user(
            username='lucas', 
            email='lucas@exemplo.com', 
            password='password123'
        )
        user2 = django_user_model.objects.create_user(
            username='outro_dev', 
            email='dev@exemplo.com', 
            password='password123'
        )
        
        Task.objects.create(title="Minha Tarefa", owner=user1)
        Task.objects.create(title="Tarefa Alheia", owner=user2)
        
        api_client.force_authenticate(user=user1)
        
        # --- ACT ---
        url = reverse('task-list')
        response = api_client.get(url)
        
        # --- ASSERT ---
        assert response.status_code == status.HTTP_200_OK
        # Verificamos se a paginação está funcionando e se retornou apenas 1
        assert response.data['count'] == 1 
        assert response.data['results'][0]['title'] == "Minha Tarefa"

    def test_sharing_task_makes_it_visible_to_other_user(self, api_client, django_user_model):
        # --- ARRANGE ---
        # 1. Criar dois utilizadores
        user_owner = django_user_model.objects.create_user(
            username='dono', email='dono@teste.com', password='pass'
        )
        user_guest = django_user_model.objects.create_user(
            username='convidado', email='convidado@teste.com', password='pass'
        )

        # 2. O 'dono' cria uma tarefa (não partilhada inicialmente)
        task = Task.objects.create(title="Tarefa Secreta", owner=user_owner)

        # 3. Validar que o 'convidado' NÃO vê a tarefa
        api_client.force_authenticate(user=user_guest)
        url = reverse('task-list')
        response_before = api_client.get(url)
        assert response_before.data['count'] == 0

        # --- ACT ---
        # 4. O 'dono' partilha a tarefa com o 'convidado' via PATCH
        api_client.force_authenticate(user=user_owner)
        detail_url = reverse('task-detail', args=[task.id])
        api_client.patch(detail_url, {'shared_with': [user_guest.id]}, format='json')

        # --- ASSERT ---
        # 5. O 'convidado' agora deve ver a tarefa na sua lista
        api_client.force_authenticate(user=user_guest)
        response_after = api_client.get(url)
        
        assert response_after.status_code == status.HTTP_200_OK
        assert response_after.data['count'] == 1
        assert response_after.data['results'][0]['title'] == "Tarefa Secreta"