from rest_framework import serializers
from .models import Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_isbn(self, value):
        if not value.isdigit():     # check if it has letters
            raise serializers.ValidationError("The ISBN can only contain numbers.")
        if len(value) != 13:        # checks if it has 13 digits or not.
            raise serializers.ValidationError("The ISBN must have 13 digits.")
        return value
    
    def validate_pages(self, value):
        if value <= 0:   
            raise serializers.ValidationError("You need to have at least one page.")
        return value
    
    def validate_published_date(self,value):
        today = date.today()
        if value > today:
            raise serializers.ValidationError("The publication date cannot be in the future.")
        return value