from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'pages', 'available', 'published_date')  # table columns
    search_fields = ('title', 'isbn')   # part of the search by title, you can add more
    list_filter = ('available','published_date')   # Side search filters, in this case by date, can add more.

admin.site.register(Book, BookAdmin)   # register student in admin