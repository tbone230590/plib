from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer
from rest_framework.response import Response

@api_view(['GET'])
@renderer_classes((StaticHTMLRenderer,))
def home(request):
    #books = Book.objects.all()
    #serializer = BookSerializer(books, many=True)
    data ="<html><body><h1>Hello API !</h1></body></html>"
    return Response(data)
