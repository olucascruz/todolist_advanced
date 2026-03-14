from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Por enquanto, usaremos o padrão, mas ter nossa classe 
    # permite expansão futura sem quebrar o banco.
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username