from django.test import TestCase
from .models import Course
from .serializers import CourseSerializer
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class CourseModelTest(TestCase):
    def test_create_course(self):
        course = Course.objects.create(
            title='biology',
            description='Best biology class',
            duration= 2,
            price= 100,
            level= 'A'
        )
        self.assertEqual(course.title, 'biology')
        self.assertEqual(str(course), 'biology')

    def test_invalid_duration (self):
        data = {
            'title':'biology',
            'description':'Best biology class',
            'duration': 0,
            'price': 100,
            'level': 'A'
        }
        serializer = CourseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('duration', serializer.errors)

    def test_negative_price(self):
        data = {
            'title':'biology',
            'description':'Best biology class',
            'duration': 2,
            'price': 0,
            'level': 'A'
        }
        serializer = CourseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('price', serializer.errors)

class CourseAPITest(APITestCase):
    def setUp(self):
        # Create the test user.
        self.user =User.objects.create_user(username='testuser', password='testpass123')  
        # generates JWT token
        refresh = RefreshToken.for_user(self.user) # Here you create the access token.
        self.token = str(refresh.access_token) # Here the created token is retrieved and displayed as a string.

        # Configure authentication on the client.
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}') # This shows that to enter, an HTTP request is made, using a bearer before the token to achieve login.
    
    def test_get_course_list(self):
        Course.objects.create(
            title='chemical',
            description='Best chemistry class',
            duration= 3,
            price= 120,
            level= 'I'
        )
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_post_create_course(self):
        data = {
            'title':'physical',
            'description':'Best physics class',
            'duration': '5',
            'price': '110',
            'level': 'A'
        }
        response = self.client.post('/courses/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(response.data['title'], 'physical')

    def test_get_course_specific(self):
        data = Course.objects.create(
            title='geography',
            description='Best geography class',
            duration= 4,
            price= 90,
            level= 'B'
        )
        response = self.client.get(f'/courses/{data.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'geography')

    def test_get_without_authentication(self):
        self.client.credentials()
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 401)

