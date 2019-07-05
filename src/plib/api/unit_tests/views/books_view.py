from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from api.data.serializers.book_serializer import BookSerializer
from api.data.models.book import Book

class BooksViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_create_book_succeeded(self):
        self.book = Book(title='Programming in Python', author='Unknown', price=200)
        serializer = BookSerializer(self.book, many=False)
        #if serializer.is_valid()

        response = self.client.post(
            reverse('list_or_create_book'),
            serializer.data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    # imvalid model author ->auther
    def test_create_book_bad_request(self):
        book = {
            'title' : 'Great',
            'auther' :'Unknown',
            'price' : 100
        }

        response = self.client.post(
            reverse('list_or_create_book'),
            book,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

