from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','cpf','date_of_birth', 'phone_number')   # table columns
    search_fields = ('name', 'email')   # search by name or email, can add more fields
    list_filter = ('date_of_birth',)   # sidebar filters, in this case by date, can add more

admin.site.register(Student, StudentAdmin)   # register Student in admin panel