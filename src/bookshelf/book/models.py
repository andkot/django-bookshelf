from django.db import models
from ..books_owner.models import BooksOwner

class Book(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(BooksOwner, on_delete=models.CASCADE)

