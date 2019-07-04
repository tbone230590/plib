from django.test import TestCase
from api.data.models.book import Book

class BookTestCase(TestCase):
    def setUp(self):
        self.title = "Programming in C"
        self.author = "Balagurusamy"
        self.price = 200
        self.book = Book(title = self.title, author = self.author, price = self.price)
    
    def test(self):
        print('test 1')
        self.assertNotEqual(1, 2)
    
    def test_validate_model(self):
        current_books_count = Book.objects.count()
        self.book.save()
        new_books_count = Book.objects.count()
        self.assertNotEqual(current_books_count, new_books_count)



