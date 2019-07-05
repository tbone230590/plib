from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer
from rest_framework.response import Response
from api.data.serializers.book_serializer import BookSerializer
from api.data.models.book import Book
from api.data.repositories.books_repository import BookRepository

# /books
# Get all books
@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def get_all_or_create(request):
    books_repository =  BookRepository()
    if request.method == 'GET':
        books = books_repository.get_all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data_to_return = {'message':'created successfully'}
            return Response(data=data_to_return, status=status.HTTP_201_CREATED)
        else:
            data_to_return = {'message':'failed to save the book'}
            return Response(data=data_to_return, status=status.HTTP_400_BAD_REQUEST)


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