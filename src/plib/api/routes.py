from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BooksView, BookDetailView

urlpatterns = {
    path('books/', BooksView.as_view(), name="list_books"),
    path('books/<int:id>', BookDetailView.as_view(), name="book_details"),
}
