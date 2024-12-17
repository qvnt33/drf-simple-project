from .models import Article
from .serializers import ArticleSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    """ModelViewSet автоматично надає CRUD дії для моделі:
    GET /articles/ -> list (список статей)
    POST /articles/ -> create (створити статтю)
    GET /articles/{id}/ -> retrieve (отримати конкретну статтю)
    PUT /articles/{id}/ -> update (оновити повністю)
    PATCH /articles/{id}/ -> partial_update (оновити частково)
    DELETE /articles/{id}/ -> destroy (видалити статтю)

    permission_classes = [IsAuthenticatedOrReadOnly]:
    - Неавторизовані користувачі можуть лише переглядати (GET), а не створювати/оновлювати/видаляти.
    - Авторизовані користувачі можуть виконувати всі дії.
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Додавання фільтрації та сортування
    filter_backends: list = [DjangoFilterBackend, OrderingFilter]
    filterset_fields: list[str] = ['article']  # Поля для фільтрації
    ordering_fields: str = '__all__'  # Сортування за всіма полями
    ordering: list[str] = ['created_at']  # Сортування за замовчуванням

    # ordering_fields = ['created_at', 'title']  # Поля, доступні для сортування
    # ordering = ['-created_at']  # Сортування за замовчуванням у зворотньому порядку
