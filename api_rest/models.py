from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    
    user_nickname = models.CharField(primary_key=True, max_length=100, default='')
    user_email = models.EmailField(default='')
    user_password = models.CharField(default='', max_length=100)

    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email} | Password: {self.user_password}'
    
class Ator(models.Model):
    nome = models.CharField(max_length=100)

class Diretor(models.Model):
    nome = models.CharField(max_length=100)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    sinopse = models.TextField()
    atores = models.ManyToManyField(Ator)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo