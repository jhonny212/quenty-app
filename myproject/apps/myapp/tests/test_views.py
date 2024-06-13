from django.test import TestCase
from rest_framework.test import APIClient
from apps.myapp.models import Author,Book
from datetime import date

class AuthorViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author_data = {'name': 'Test Author', 'birth_date': '2000-01-01'}
        self.author = Author.objects.create(name='Test Author', birth_date='2000-01-01')

    def test_author_list(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_author(self):
        response = self.client.post('/api/authors/', self.author_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Author.objects.count(), 2)

    def test_retrieve_author(self):
        response = self.client.get(f'/api/authors/{self.author.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Author')

    def test_update_author(self):
        updated_data = {'name': 'Updated Author', 'birth_date': '2001-01-01'}
        response = self.client.put(f'/api/authors/{self.author.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, 'Updated Author')

    def test_delete_author(self):
        response = self.client.delete(f'/api/authors/{self.author.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Author.objects.count(), 0)

class BookViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='Test Author', birth_date='2000-01-01')
        self.book_data = {
            'title': 'Test Book',
            'published_date': '2022-01-01',
            'author': self.author.id,
            'rating': 4.5
        }
        self.book = Book.objects.create(
            title='Test Book',
            published_date=date(2022, 1, 1),
            author=self.author,
            rating=4.5
        )

    def test_book_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_book(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        updated_data = {
            'title': 'Updated Book',
            'published_date': '2023-01-01',
            'author': self.author.id,
            'rating': 4.0
        }
        response = self.client.put(f'/api/books/{self.book.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Book.objects.count(), 0)