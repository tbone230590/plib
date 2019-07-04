# Book Model
from django.db import models
from django.utils.timezone import timezone

class Book(models.Model):
    """ This class represents Book model """
    title = models.CharField(max_length = 255, blank = False)
    author = models.CharField(max_length = 50, blank = False)
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        """ String representation of Book model class"""
        return "Book(Title: {}, Author:{}, Price: {}, Date Created: {}, Date Modified: {})".format(
                self.title, 
                self.author, 
                self.price, 
                self.date_created, 
                self.date_modified
            )