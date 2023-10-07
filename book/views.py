# Create your views here.

from django.shortcuts import render
from .models import Book

def book_home_page(request):
    return render(request, "book_home.html")

def filter_book(request):
    search_book = request.POST.get('search_book', '')
    authors = request.POST.getlist('authors')
    descriptions = request.POST.getlist('description')

    book = Book.objects.all()

    if not search_book:
        return render(request, 'books.html', {'books': book, 'search_book': search_book})


    if authors:
        book = book.filter(author__in=authors)

    if descriptions:
        book = book.filter(description__in=descriptions)

    book = book.filter(name__icontains=search_book)

    return render(request, 'books.html', {'books': book, 'search_book': search_book})