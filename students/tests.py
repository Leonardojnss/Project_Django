from django.test import TestCase
from .models import Student
from datetime import date
from .serializers import StudentSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

class StudentModelTest(TestCase):
    def test_create_student(self):   # places Student model objects into student variable (Student.objects) and uses create to create test student
        student = Student.objects.create(
            name="Bia",
            email="bia@bia.com",
            cpf="32165498700",
            date_of_birth=date(2000, 1, 1),
            phone_number="10231589731"
        )
        self.assertEqual(student.name, "Bia") 
        self.assertEqual(str(student), "Bia")

    def test_invalid_cpf(self):
    # tries to create student with invalid CPF
        data = {
            'name':'Teste Inválido',
            'email':'invalido@teste.com',
            'cpf':'123',  # invalid CPF (too short)
            'date_of_birth':date(2000, 1, 1),
            'phone_number':'11999999999'
        }
    
        serializer = StudentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('cpf', serializer.errors)

    
    def test_underage_student(self):
        data = {
            'name':'Teste dois',
            'email':'testedois@teste.com',
            'cpf':'21321321321', 
            'date_of_birth':date(2010, 1, 1),
            'phone_number':'11999999129'
            }
        serializer = StudentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('date_of_birth', serializer.errors)

    def test_invalid_phone(self):
        data = {
            'name':'teste tres',
            'email':'testetres@teste.com',
            'cpf':'65748392011',
            'date_of_birth':date(2010, 1, 1),
            'phone_number':'123'
        }
        serializer = StudentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('phone_number', serializer.errors)

class StudentAPITest(APITestCase):
    def setUp(self):
        # creates test user
        self.user =User.objects.create_user(username='testuser', password='testpass123')  
        # generates JWT token
        refresh = RefreshToken.for_user(self.user) # creates access token here
        self.token = str(refresh.access_token) # gets created token and displays as string

        # configures authentication on client
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}') # shows that to enter comes HTTP request using bearer before token to be able to enter

    def test_get_student_list(self):
        # creates a student
        Student.objects.create(
            name=" student",
            email="test@test.com",
            cpf="12345678901",
            date_of_birth=date(2000, 1, 1),
            phone_number="10231589731"
        )
        response = self.client.get('/students/')   # makes a GET /students/
        # verifies success
        self.assertEqual(response.status_code, 200)  #  verifies if HTTP status code of response is 200 (OK)
        self.assertEqual(len(response.data), 1)  # verifies if API returned exactly 1 student in list

    def test_post_create_student(self):
        data = {
            'name':'New student',
            'email':'new@student.com',
            'cpf':'98765432100',
            'date_of_birth':'2001-05-05',
            'phone_number':'11988887777'
        }
        response = self.client.post('/students/', data, format='json')  # makes a POST /students/ using test data in json

        self.assertEqual(response.status_code, 201) #  201 = Created
        self.assertEqual(Student.objects.count(),1)   # counts in database
        self.assertEqual(response.data['name'], 'New student')   # Vverifies returned data

    def test_get_student_specific(self):
        data = Student.objects.create(
            name="test 1 more",
            email="test@more.com",
            cpf="32160098700",
            date_of_birth=date(2000, 1, 1),
            phone_number="10231009731"
        )
        response = self.client.get(f'/students/{data.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'test 1 more')
    
    def test_get_without_authentication(self):
        self.client.credentials()
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 401)
        