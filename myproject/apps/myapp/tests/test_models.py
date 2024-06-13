from django.test import TestCase
from datetime import date
from apps.myapp.models import Author, Book

class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author", birth_date=date(2023, 1, 1))

    def test_author_creation(self):
        author = Author.objects.get(id=self.author.id)
        self.assertEqual(author.name, "Test Author")
        self.assertEqual(author.birth_date, date(2023, 1, 1))

    def test_author_str_method(self):
        self.assertEqual(str(self.author), "Test Author")

    def test_author_update(self):
        self.author.name = "Updated Author"
        self.author.save()
        author = Author.objects.get(id=self.author.id)
        self.assertEqual(author.name, "Updated Author")

    def test_author_delete(self):
        self.author.delete()
        with self.assertRaises(Author.DoesNotExist):
            Author.objects.get(id=self.author.id)

class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author", birth_date=date(2023, 1, 1))
        self.book = Book.objects.create(title="Test Book", published_date=date(2020, 1, 1), author=self.author, rating=4.5)

    def test_book_creation(self):
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.published_date, date(2020, 1, 1))
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.rating, 4.5)

    def test_book_str_method(self):
        self.assertEqual(str(self.book), "Test Book")

    def test_book_update(self):
        self.book.title = "Updated Book"
        self.book.rating = 5.0
        self.book.save()
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(book.title, "Updated Book")
        self.assertEqual(book.rating, 5.0)

    def test_book_delete(self):
        self.book.delete()
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=self.book.id)