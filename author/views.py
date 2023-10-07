# Create your views here.
from django.shortcuts import render, redirect
def author_home_page(request):
    return render(request, "author_home.html")