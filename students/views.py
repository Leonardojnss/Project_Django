from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()      # gets all objects from database only from Students section 
    serializer_class = StudentSerializer  # indicates which serializer it will use
    permission_classes = [IsAuthenticated]  # requires JWT authentication to access