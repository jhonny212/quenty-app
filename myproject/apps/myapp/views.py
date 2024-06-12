from rest_framework import viewsets
from apps.myapp.models import Author, Book
from apps.myapp.serializers import AuthorSerializer, BookSerializer
from django_filters import rest_framework as filters
from apps.myapp.filters import  BookFilter

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter