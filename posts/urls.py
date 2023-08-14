from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

router = SimpleRouter()

router.register('', PostViewSet, basename='posts')

router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls


# from . import views

# urlpatterns = [
#     path('<int:pk>/', views.PostDetail.as_view()),
#     path('', views.PostList.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]