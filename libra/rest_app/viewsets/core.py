from rest_framework import viewsets

from core.models import Book
from rest_app.serializers.core import BookSerializer


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer