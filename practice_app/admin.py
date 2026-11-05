from django.contrib import admin
from .models import Book, Comment, Author, Category, Reader, Release, Isbn

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Reader)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Release)
admin.site.register(Isbn)

