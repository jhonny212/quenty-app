from django.test import TestCase
from apps.myapp.models import Author, Book
from apps.myapp.filters import BookFilter
from datetime import date

class BookFilterTestCase(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(name='Test Author 1', birth_date='2000-01-01')
        self.author2 = Author.objects.create(name='Test Author 2', birth_date='2001-05-05')

        self.book1 = Book.objects.create(title='Book 1', published_date=date(2022, 1, 1), author=self.author1, rating=4.5)
        self.book2 = Book.objects.create(title='Book 2', published_date=date(2022, 2, 1), author=self.author2, rating=3.5)

    def test_book_filter_author_name(self):
        queryset = Book.objects.all()
        params = {'author__name__icontains': 'Test Author'}
        book_filter = BookFilter(params, queryset=queryset)
        filtered_books = book_filter.qs
        self.assertEqual(len(filtered_books), 2)
        self.assertEqual(filtered_books.first().title, 'Book 1')

    def test_book_filter_published_date(self):
        queryset = Book.objects.all()
        params = {'published_date': '2022-01-01'}
        book_filter = BookFilter(params, queryset=queryset)
        filtered_books = book_filter.qs
        self.assertEqual(len(filtered_books), 1)
        self.assertEqual(filtered_books.first().title, 'Book 1')

    def test_book_filter_combined(self):
        queryset = Book.objects.all()
        params = {'author__name__icontains': 'Test Author', 'published_date': '2022-01-01'}
        book_filter = BookFilter(params, queryset=queryset)
        filtered_books = book_filter.qs
        self.assertEqual(len(filtered_books), 1)
        self.assertEqual(filtered_books.first().title, 'Book 1')