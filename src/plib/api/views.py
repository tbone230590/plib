from rest_framework import generics, renderers
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.generic import TemplateView
from api.data.serializers.book_serializer import BookSerializer
from api.data.models.book import Book

#books/
class BooksView(APIView):
    """This class defines the create behavior of our rest api."""
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        return JsonResponse("{'delete':'arul'}", safe=False)

class BookDetailView(APIView):
    def get(self, request, id):
        book = Book(id=100, title='Book', author='Arul', price=100)
        serializer = BookSerializer(book, many=False)
        return JsonResponse(serializer.data, safe=False)