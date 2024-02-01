from rest_framework import serializers
from .models import User,Filme,Ator,Diretor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ator
        fields = ['nome']


class DiretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretor
        fields = ['nome']

class FilmeSerializer(serializers.ModelSerializer):
    atores = AtorSerializer(read_only=True, many=True)
    diretor = DiretorSerializer(read_only=True)
    
    class Meta:
        model = Filme
        fields = '__all__'