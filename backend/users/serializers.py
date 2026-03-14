from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # A senha é apenas para escrita, nunca deve ser retornada no JSON
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # O método create_user faz o hash da senha automaticamente (Segurança!)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user