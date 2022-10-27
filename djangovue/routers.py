from rest_framework import routers
from core.viewsets import ArticleViewSet,UserViewSet



router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'users',UserViewSet )