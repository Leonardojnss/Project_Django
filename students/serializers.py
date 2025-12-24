from rest_framework import serializers
from .models import Student
from datetime import date
import re    # Python library for using regex

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_cpf(self,value):
        if not value.isdigit():      # validate if it contains letters
            raise serializers.ValidationError("CPF must contain only numbers")   # raise prevents proceeding unless data is correct
        if len(value) != 11:                  # validate if it has 11 characters
            raise serializers.ValidationError("CPF must have 11 digits.")      # raise prevents proceeding unless data is correct
        return value  # after passing correct data, it will return the values
    
    def validate_date_of_birth(self,value):
        today = date.today()
        age = today.year - value.year
        if (today.month, today.day) < (value.month, value.day): #  just to check if birthday has already passed or not
            age -= 1
        if age < 16:    # this is where validation happens
            raise serializers.ValidationError(f"Student must be at least 16 years old, you are still {age} years old. ")
        return value

    def validate_phone_number(self,value):
        phone_clean = re.sub(r'[^0-9]', '', value)   # r'[^0-9]' -> this is regex / clean special characters 
        if len(phone_clean) < 10 or len(phone_clean) > 11:
            raise serializers.ValidationError("The phone number must have 10 or 11 digits.")
        return value
