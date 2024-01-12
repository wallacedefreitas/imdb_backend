from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User,UserComments
from .serializers import UserSerializer, CommentSerializer


import json


@api_view(['GET','POST'])
def user_manager(request):

    if request.method == 'POST':

        new_user = request.data
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':

        try:
            if request.data['user_nickname']:                         

                user_nickname = request.data['user_nickname']         

                try:
                    user = User.objects.get(pk=user_nickname)   
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UserSerializer(user)           
                return Response(serializer.data)            

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_users(request):

    if request.method == 'GET':

        users = User.objects.all()                          

        serializer = UserSerializer(users, many=True)       

        return Response(serializer.data)                   
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT','DELETE'])
def comment_manager(request):

    if request.method == 'GET':

        try:

            if request.data['airbnb_name'] and request.data["user_nickname"]:

                airbnb = request.data['airbnb_name']
                nickname = request.data["user_nickname"]

                try:
                    comment = UserComments.objects.get(airbnb_name=airbnb, user_nickname=nickname)

                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = CommentSerializer(comment)
                return Response(serializer.data)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':

        new_comment = request.data
        
        serializer = CommentSerializer(data=new_comment)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':

        airbnb = request.data['airbnb_name']
        nickname = request.data["user_nickname"]
        try:
            updated_comment = UserComments.objects.get(airbnb_name=airbnb, user_nickname=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(updated_comment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':

        try:
            airbnb = request.data['airbnb_name']
            nickname = request.data["user_nickname"]
            
            comment_to_delete = UserComments.objects.get(airbnb_name=airbnb, user_nickname=nickname)
            comment_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_comments(request):
    
    if request.method == 'GET':

        comments = UserComments.objects.all()                          
        serializer = CommentSerializer(comments, many=True)       
        return Response(serializer.data)                   
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def hello_world(request):
    if request.method == 'GET':
        return Response({"message": "Hello_World"})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)