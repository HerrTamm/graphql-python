import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from users.models import User, FavouriteBooks, Book

class UserType(DjangoObjectType):
    class Meta:
        model = User

class FavouriteBooksType(DjangoObjectType):
    class Meta:
        model = FavouriteBooks

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Query(ObjectType):
    favouriteBooks = graphene.List(FavouriteBooksType, username=graphene.String())

    def resolve_favouriteBooks(self, info, **kwargs):
        username = kwargs.get('username')

        if (username is not None):
            return FavouriteBooks.objects.all().filter(username=username)

        return None

schema = graphene.Schema(query=Query)