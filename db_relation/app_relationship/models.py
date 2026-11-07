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
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book', related_name='authors')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Writer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book', related_name='writers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


