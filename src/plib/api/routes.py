from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import books_view, home_view
#from .views import BooksView, BookDetailView

urlpatterns = {
    path('books/', books_view.get_all, name="list_books"),
    path('books/<int:id>', books_view.get_by_id, name="book_detail"),
    path('', home_view.home, name="home"),
    #path('books/<int:id>', BookDetailView.as_view(), name="book_details"),
}
