from django.test import TestCase
from apps.myapp.models import Author
from apps.myapp.serializers import AuthorSerializer
import datetime

class AuthorSerializerTestCase(TestCase):
    def setUp(self):
        self.author_data = {'name': 'Test Author', 'birth_date': '2001-01-01'}
        self.author = Author.objects.create(name='Test Author', birth_date='2001-01-01')

    def test_author_serializer_valid(self):
        serializer = AuthorSerializer(instance=self.author)
        self.assertEqual(serializer.data['name'], 'Test Author')
        self.assertEqual(serializer.data['birth_date'], '2001-01-01')

    def test_author_serializer_create(self):
        serializer = AuthorSerializer(data=self.author_data)
        self.assertTrue(serializer.is_valid())
        author = serializer.save()
        self.assertEqual(author.name, 'Test Author')
        self.assertEqual(author.birth_date, datetime.date(2001,1,1))