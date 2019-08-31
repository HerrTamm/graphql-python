from django.db import models
from uuid import uuid4

class User(models.Model):
    username = models.CharField(max_length=20, unique=True, primary_key=True)
    password = models.CharField(max_length=60)
    email = models.EmailField(max_length=254, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.username

class FavouriteBooks(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=False, primary_key=True)
    username = models.CharField(max_length=20)
    book = models.UUIDField(default=uuid4, editable=False, unique=False)

    class Meta:
        unique_together = [['username', 'book']]
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['book']),
        ]

class Book(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=False, primary_key=True)
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    released = models.DateField()