from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
#from .views import BooksView, BookDetailView

urlpatterns = {
    path('books/', views.get_all_books, name="list_books"),
    path('', views.home, name="home"),
    #path('books/<int:id>', BookDetailView.as_view(), name="book_details"),
}
