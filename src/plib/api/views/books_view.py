from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer
from rest_framework.response import Response
from api.data.serializers.book_serializer import BookSerializer
from api.data.models.book import Book
from api.data.repositories.books_repository import BookRepository

# /books
# Get all books
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_all(request):
    books_repository =  BookRepository()
    books = books_repository.get_all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# /books/<int:id>
# Get book details by book id
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_by_id(request, id):
    print('Book Id'+ str(id))
    
    try:
        books_repository =  BookRepository()
        book = books_repository.get_by_id(id)
        serializer = BookSerializer(book, many=False)
        data_return = serializer.data
    except:
        print('no book found for id' + str(id))
        data_return = {}
    
    return Response(data_return)