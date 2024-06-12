from django.contrib import admin
from apps.myapp.models import Author,Book
# Register your models here.

admin.site.register([Author,Book])