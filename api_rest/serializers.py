from rest_framework import serializers

from .models import User ,UserComments



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComments
        fields = '__all__'
