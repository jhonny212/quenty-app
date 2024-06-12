from rest_framework import serializers
from django_filters import rest_framework as filters
from apps.myapp.models import Author, Book

class BookFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    published_date = filters.DateFilter(field_name='published_date')

    class Meta:
        model = Book
        fields = ['author', 'published_date']