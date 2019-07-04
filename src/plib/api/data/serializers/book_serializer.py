# Book Serializer
from rest_framework import serializers
from api.data.models.book import Book

class BookSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Book
        fields = ('id', 'title', 'author', 'price', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')