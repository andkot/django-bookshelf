from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    # author_name = models.CharField()
    description = models.TextField()
