from .views import ArticleViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()  # Автоматично генерує URL-шляхи для CRUD-операцій модуля
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns: list = [
    path('', include(router.urls)),  # Включення маршрутів, сформовані router
]
