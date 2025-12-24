from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("It is not possible to use negative values.")
        return value
    
    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("The duration should be at least 1 hour.")
        return value