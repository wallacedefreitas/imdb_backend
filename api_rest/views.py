from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import AuthenticationFailed

from .models import User, Ator, Diretor, Filme
from .serializers import UserSerializer, AtorSerializer, DiretorSerializer, FilmeSerializer

import json


#Atores
@api_view(['GET'])
def get_all_actors(request):
    
    try:
        atores = Ator.objects.all()
        serializer = AtorSerializer(atores, many=True)       
        return Response(serializer.data)                   
    
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_actor(request):
    try:
        if request.data.get('nome'):
            
            nome = request.data.get('nome')
            try:
                ator =  Ator.objects.get(nome__iexact=nome)

            except Ator.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = AtorSerializer(ator)
            return Response(serializer.data)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_actor(request):
    novo_ator = request.data
    nome_ator = novo_ator.get('nome', '').lower()
    ator, created = Ator.objects.get_or_create(nome=nome_ator)

    if created:
        serializer = AtorSerializer(ator)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({"detail": "Ator já existe."}, status=status.HTTP_400_BAD_REQUEST)

#Diretores
@api_view(['GET'])
def get_all_directors(request):
    
    try:
        diretores = Diretor.objects.all()                          
        serializer = DiretorSerializer(diretores, many=True)       
        return Response(serializer.data)                   
    
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_director(request):
    try:
        if request.data.get('nome'):
            nome = request.data.get('nome').lower()
            diretor, created = Diretor.objects.get_or_create(nome__iexact=nome)

            serializer = DiretorSerializer(diretor)
            return Response(serializer.data)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_director(request):
            
    novo_diretor = request.data
    nome_diretor = novo_diretor.get('nome', '').lower()
    diretor, created = Diretor.objects.get_or_create(nome=nome_diretor)

    if created:
        serializer = AtorSerializer(diretor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({"detail": "Diretor já existe."}, status=status.HTTP_400_BAD_REQUEST)

#Filmes
@api_view(['GET'])
def get_all_films(request):
    
    try:
        filmes = Filme.objects.all()                          
        serializer = FilmeSerializer(filmes, many=True)       
        return Response(serializer.data)                   
    
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_film(request):
    try:
        if request.data.get('titulo'):
            titulo = request.data.get('titulo')
            try:
                filme =  Filme.objects.get(titulo__iexact=titulo)

            except Filme.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = FilmeSerializer(filme)
            return Response(serializer.data)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_films_by_actor(request):
    if request.data.get('nome'):
            
        nome = request.data.get('nome')
        
        try:
            ator = Ator.objects.get(nome__iexact=nome)
        except Ator.DoesNotExist:
            return Response({"detail": "Ator não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        filmes = ator.filme_set.all()
        serializer = FilmeSerializer(filmes, many=True)
        return Response(serializer.data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_film(request):
    # Obtenha o token do corpo da solicitação
    token = request.data.get('token')

    if token is None:
        raise AuthenticationFailed('Token não fornecido')

    # Tente obter o token do banco de dados
    try:
        token_obj = Token.objects.get(key=token)
    except Token.DoesNotExist:
        raise AuthenticationFailed('Token inválido')

    if token_obj.user is not None:
        novo_filme = request.data

        # Verifica se o diretor já existe, se não, cria um novo
        diretor, created = Diretor.objects.get_or_create(nome=novo_filme['diretor'])

        # Cria o filme
        filme = Filme.objects.create(titulo=novo_filme['titulo'], ano=novo_filme['ano'], sinopse=novo_filme['sinopse'], diretor=diretor)

        # Adiciona os atores
        for nome_ator in novo_filme['atores']:
            ator, created = Ator.objects.get_or_create(nome=nome_ator)
            filme.atores.add(ator)

        serializer = FilmeSerializer(filme)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_film(request):
    # Obtenha o token do corpo da solicitação
    token = request.data.get('token')

    if token is None:
        raise AuthenticationFailed('Token não fornecido')

    # Tente obter o token do banco de dados
    try:
        token_obj = Token.objects.get(key=token)
    except Token.DoesNotExist:
        raise AuthenticationFailed('Token inválido')

    if token_obj.user is not None:
        # Verifica se o título está presente nos parâmetros da requisição
        if not request.data.get('titulo'):
            return Response({"detail": "Parâmetro 'titulo' não encontrado."}, status=status.HTTP_400_BAD_REQUEST)

        titulo = request.data.get('titulo')

        # Tenta obter o filme pelo título
        try:
            filme = Filme.objects.get(titulo__iexact=titulo)
        except Filme.DoesNotExist:
            return Response({"detail": f"Filme com título '{titulo}' não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Deleta o filme
        filme.delete()

        return Response({"detail": f"Filme com título '{titulo}' deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_film(request):
    # Obtenha o token do corpo da solicitação
    token = request.data.get('token')

    if token is None:
        raise AuthenticationFailed('Token não fornecido')

    # Tente obter o token do banco de dados
    try:
        token_obj = Token.objects.get(key=token)
    except Token.DoesNotExist:
        raise AuthenticationFailed('Token inválido')

    if token_obj.user is not None:
        try:
            novo_filme = request.data
            filme = Filme.objects.get(titulo=novo_filme['titulo'])
        except Filme.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data

        # Atualiza o diretor, se fornecido
        if 'diretor' in data:
            diretor, created = Diretor.objects.get_or_create(nome=data['diretor'])
            filme.diretor = diretor

        # Atualiza os atores, se fornecidos
        if 'atores' in data:
            filme.atores.clear()
            for nome_ator in data['atores']:
                ator, created = Ator.objects.get_or_create(nome=nome_ator)
                filme.atores.add(ator)

        # Atualiza os outros campos
        if 'ano' in data:
            filme.ano = data['ano']
        if 'sinopse' in data:
            filme.sinopse = data['sinopse']

        filme.save()

        serializer = FilmeSerializer(filme)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Usuário
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    token = Token.objects.create(user=user)

    return Response({'token': token.key}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid login credentials'}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout(request):
    # Obtenha o token do corpo da solicitação
    token = request.data.get('token')

    if token is None:
        raise AuthenticationFailed('Token não fornecido')

    # Tente obter o token do banco de dados
    try:
        token_obj = Token.objects.get(key=token)
    except Token.DoesNotExist:
        raise AuthenticationFailed('Token inválido')

    # Se o token existir, exclua-o
    token_obj.delete()
    raise AuthenticationFailed('Logout efetuado')

    return Response(status=status.HTTP_200_OK)
    # Obtenha o token do corpo da solicitação
    token = request.data.get('token')

    if token is None:
        raise AuthenticationFailed('Token não fornecido')

    # Tente obter o token do banco de dados
    try:
        token_obj = Token.objects.get(key=token)
    except Token.DoesNotExist:
        raise AuthenticationFailed('Token inválido')

    # Se o token existir e estiver associado a um usuário, retorne a mensagem
    if token_obj.user is not None:
        return Response({"message": "Hello, you are authenticated!"})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)