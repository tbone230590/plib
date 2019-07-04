from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from api.data.models.book import Book

class BooksViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def create_book_succeeded(self):
        self.book = Book(title = "Programming in Python", author = "Unknown", price = 200)
        response = self.client.post(
            reverse('create_book'),
            self.book,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

