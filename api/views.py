from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets
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
