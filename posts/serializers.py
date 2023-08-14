from rest_framework import serializers
from django.contrib.auth import get_user_model # new
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')
        
        
class CustomUserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
        ref_name = 'CustomUser'  # Provide a unique ref_name

class UserSerializer(CustomUserSerializer):
    pass