from django.db import models


class Isbn(models.Model):
    isbn = models.CharField(max_length=100)

    def __str__(self):
        return self.isbn


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.OneToOneField('Isbn', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    release_date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book', related_name='authors')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Comment(models.Model):
    author_name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=200)
    text = models.TextField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author_name} - {self.book_title}"


class Reader(models.Model):
    author_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=200)
    age = models.IntegerField()


    def __str__(self):
        return f"{self.author_name} {self.author_last_name}"


class Release(models.Model):
    book_title = models.CharField(max_length=200)
    book_author_name = models.CharField(max_length=100)
    release_date = models.DateField()

