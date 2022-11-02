from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=50)

class Author(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey(Author, null=True, on_delete= models.SET_NULL)
    description = models.CharField(max_length=1000)
    published_date = models.DateTimeField()

class Review(models.Model):
    class Raiting(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    book = models.ForeignKey(Book, null=True, related_name='reviews', on_delete= models.SET_NULL)
    text = models.CharField(max_length=1000)
    raiting = models.IntegerField(default=5, choices=Raiting.choices)

class Favourites(models.Model):
    user = models.ForeignKey(User, null=True, on_delete= models.CASCADE)
    book = models.ForeignKey(Book, related_name='in_favourites', null=True, on_delete= models.CASCADE)