from datetime import datetime
from rest_framework import serializers, viewsets
from .models import Article
from .models import Article
from .serializers import ArticleSerializer
from .serializers import UserSerializer
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
      