from django.contrib import admin
from .models import Book, Writer, Isbn, Category

admin.site.register(Book)
admin.site.register(Writer)
admin.site.register(Isbn)
admin.site.register(Category)
