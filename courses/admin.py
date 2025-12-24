from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','duration', 'price', 'level')   # table columns
    search_fields = ('title',)    # part of the search by title, you can add more
    list_filter = ('level',)    # Side search filters, in this case by date, can add more.

admin.site.register(Course,CourseAdmin)  # register student in admin
