
from django.urls import path, include
from .views import author_home_page


urlpatterns = [
    path('', author_home_page, name = "author_home_page")
]

