from django.test import TestCase
from api.data.models.issued_book import IssuedBook
from api.data.models.book import Book

class IssuedBookTestCase(TestCase):
    def setUp(self):
        # self.title = "Programming in C"
        # self.author = "Balagurusamy"
        # self.price = 200
        self.book = Book.objects.get(title="Programming in C")
        self.issue_book = IssuedBook(book=self.book)
    
    def test_validate_model(self):
        current_count = IssuedBook.objects.count()
        self.issue_book.save()
        new_count = IssuedBook.objects.count()
        self.assertEqual(current_count+1, new_count)



