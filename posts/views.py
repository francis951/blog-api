from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer, UserSerializer 
# from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model

# from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class CustomPagination(PageNumberPagination):
    page_size = 4 
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]
#     pagination_class = CustomPagination
#     filter_backends = [DjangoFilterBackend]
#     # permission_classes = (permissions.IsAuthenticated,)
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # permission_classes = (permissions.IsAuthenticated,)
#     permission_class = (IsAuthorOrReadOnly,)
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    
    
# class UserList(generics.ListCreateAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset =  Post.objects.all()
    serializer_class = PostSerializer
    permission_class = (IsAuthorOrReadOnly,)
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer