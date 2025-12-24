from django.test import TestCase
from .models import Book
from .serializers import BookSerializer
from datetime import date
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class BookModelTest(TestCase):
    def test_create_book(self):
        book = Book.objects.create(
            title='java',
            author='lucas',
            isbn='1234567891011',
            pages= 2,
            available=True,
            published_date=date(2000, 1, 1)
        )
        self.assertEqual(book.title, 'java')
        self.assertEqual(str(book), 'java')

    def test_invalid_isbn(self):
        data = {
            'title':'java',
            'author':'lucas',
            'isbn':'12345678910',
            'pages': 2,
            'available':True,
            'published_date':date(2000, 1, 1)
        }

        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('isbn', serializer.errors)
    
    def test_invalid_pages(self):
        data = {
            'title':'java',
            'author':'lucas',
            'isbn':'1234567891011',
            'pages': 0,
            'available':True,
            'published_date':date(2000, 1, 1)
        }

        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('pages', serializer.errors)

    def test_invalid_published_date(self):
        data = {
            'title':'java',
            'author':'lucas',
            'isbn':'1234567891011',
            'pages': 3,
            'available':True,
            'published_date':date(2030, 1, 1)
        }
        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('published_date', serializer.errors)

class BookAPITest(APITestCase):
    def setUp(self):
        # Create the test user.
        self.user =User.objects.create_user(username='testuser', password='testpass123')  
        # generates JWT token
        refresh = RefreshToken.for_user(self.user) # Here you create the access token.
        self.token = str(refresh.access_token) # Here, the created token is retrieved and displayed as a string.

        # Configure authentication on the client.
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}') # This shows that to enter, an HTTP request is made, using a bearer before the token to achieve login.

    def test_get_book_list(self):
        Book.objects.create(
            title='teste 1',
            author='testbook',
            isbn='1234567891201',
            pages= 2,
            available=True,
            published_date=date(2000, 2, 4)
        )
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data),1)

    def test_post_create_book(self):
        data = {
            'title':'teste 2',
            'author':'testbook2',
            'isbn':'2234567892201',
            'pages': '2',
            'available':'True',
            'published_date':'2000-10-04'
        }
        response = self.client.post('/books/',data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(response.data['title'],'teste 2')

    def test_get_book_specific(self):
        data = Book.objects.create(
            title='teste 3',
            author='testbook3',
            isbn='1239567891201',
            pages= 2,
            available=True,
            published_date=date(2012, 1, 12)
        )
        response = self.client.get(f'/books/{data.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'teste 3')
    
    def test_get_without_authentication(self):
        self.client.credentials()
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 401)
