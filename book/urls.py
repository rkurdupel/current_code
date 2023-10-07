from django.urls import path
from .views import filter_book, book_home_page

urlpatterns = [
    path('', book_home_page, name = "book_home_page"),
    path('books/', filter_book, name = 'filter_book'),
]