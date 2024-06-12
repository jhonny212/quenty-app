from django.db import models
from django.core.validators import MinValueValidator

class Author(models.Model):
    """Model definition for Author."""

    name = models.CharField("Author Name", max_length=100, null=False, blank=False)
    birth_date = models.DateField("Birthdate", auto_now=False, auto_now_add=False, null=False, blank=False)

    class Meta:
        """Meta definition for Author."""

        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """Model definition for Book."""

    title = models.CharField("Title", max_length=200)
    published_date = models.DateField("Published Date", auto_now=False, auto_now_add=False)
    author = models.ForeignKey(Author, related_name="books_author", on_delete=models.CASCADE, null=False)
    rating = models.FloatField("Rating", validators=[MinValueValidator(0)])

    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


