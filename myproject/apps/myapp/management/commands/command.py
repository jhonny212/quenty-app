from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.myapp.models import Author, Book
from django.db.models import Avg
from datetime import timedelta

class Command(BaseCommand):
    help = 'Execute advanced ORM queries'

    def handle(self, *args, **kwargs):
        #Retrieve all authors who have written a book with a rating greater than 4.5.
        authors_with_high_rated_books = Author.objects.filter(books_author__rating__gt=4.5).distinct()
        self.stdout.write("Authors with books rated higher than 4.5:")
        for author in authors_with_high_rated_books:
            self.stdout.write(f"{author.name}")

        #Retrieve all books published in the last year.
        one_year_ago = timezone.now() - timedelta(days=365)
        recent_books = Book.objects.filter(published_date__gte=one_year_ago)
        self.stdout.write("\nBooks published in the last year:")
        for book in recent_books:
            self.stdout.write(f"{book.title} Published on {book.published_date}")

        #Calculate the average rating of books for each author and order the authors by their average rating in descending order.
        authors_avg_rating = Author.objects.annotate(avg_rating=Avg('books_author__rating')).order_by('-avg_rating')
        self.stdout.write("\nAuthors ordered by average book rating:")
        for author in authors_avg_rating:
            self.stdout.write(f"{author.name} With Average rating: {author.avg_rating:.4f}")