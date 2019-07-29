# Book Model
from django.db import models
from django.utils.timezone import timezone

from api.data.models.book import Book

class IssuedBook(models.Model):
    """ This class represents Issued Book model """
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
