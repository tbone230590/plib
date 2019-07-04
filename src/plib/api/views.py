# from rest_framework import generics
# from rest_framework import status
# from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer
# from rest_framework.response import Response
# from django.views.generic import TemplateView
# from api.data.serializers.book_serializer import BookSerializer
# from api.data.models.book import Book


# @api_view(['GET'])
# @renderer_classes((JSONRenderer,))
# def get_all_books(request):
#     #books = Book.objects.all()
#     #serializer = BookSerializer(books, many=True)
#     data ={'Test':'Hai'}
#     return Response(data)

# @api_view(['GET'])
# @renderer_classes((StaticHTMLRenderer,))
# def home(request):
#     #books = Book.objects.all()
#     #serializer = BookSerializer(books, many=True)
#     data ="<html><body><h1>Hello API !</h1></body></html>"
#     return Response(data)
#     # def post(self, request):
#     #     serializer = BookSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # def delete(self, request):
#     #     return JsonResponse("{'delete':'arul'}", safe=False)

# # class BookDetailView(APIView):
# #     def get(self, request, id):
# #         book = Book(id=100, title='Book', author='Arul', price=100)
# #         serializer = BookSerializer(book, many=False)
# #         return JsonResponse(serializer.data, safe=False)