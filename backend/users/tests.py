import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

# Definimos o modelo de usuário atual (o seu Custom User)
User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
class TestUserAuth:
    
    def test_user_can_register(self, api_client):
        # --- ARRANGE ---
        url = reverse('register')
        data = {
            "username": "novo_usuario",
            "email": "novo@teste.com",
            "password": "senha_segura_123"
        }

        # --- ACT ---
        response = api_client.post(url, data, format='json')

        # --- ASSERT ---
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['username'] == "novo_usuario"
        # Segurança: a senha não deve vir no JSON
        assert 'password' not in response.data 
        # Verifica se o usuário foi realmente criado no banco
        assert User.objects.filter(username="novo_usuario").exists()

    def test_user_login_returns_jwt_token(self, api_client):
        # --- ARRANGE ---
        # Criamos um usuário primeiro
        User.objects.create_user(username='lucas', password='password123', email='lucas@teste.com')
        url = reverse('token_obtain_pair')
        data = {
            "username": "lucas",
            "password": "password123"
        }

        # --- ACT ---
        response = api_client.post(url, data, format='json')

        # --- ASSERT ---
        assert response.status_code == status.HTTP_200_OK
        # O SimpleJWT deve retornar 'access' e 'refresh'
        assert 'access' in response.data
        assert 'refresh' in response.data