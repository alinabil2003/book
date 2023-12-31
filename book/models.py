from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


# author
class Author(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    biography = models.TextField(max_length=500, null=False, blank=True)

    def __str__(self):
        return self.name


# book
class Book(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()

    def __str__(self):
        return self.title


# review
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    reviewer_name = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(max_length=500, null=False, blank=False)
    rating = models.IntegerField()

    def __str__(self):
        return self.reviewer_name
