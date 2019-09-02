from django.db import models
from uuid import uuid4

class User(models.Model):
    username = models.CharField(max_length=20, unique=True, primary_key=True)
    password = models.CharField(max_length=60)
    email = models.EmailField(max_length=254, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.username

class Book(models.Model):
    book_uuid = models.UUIDField(default=uuid4, editable=False, unique=False, primary_key=True)
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    released = models.DateField()

    def __str__(self):
        return self.book_uuid

class FavouriteBooks(models.Model):
    favourite_books_uuid = models.UUIDField(default=uuid4, editable=False, unique=False, primary_key=True)
    username = models.CharField(max_length=20)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.favourite_books_uuid

    class Meta:
        unique_together = [['username', 'book']]
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['book']),
        ]