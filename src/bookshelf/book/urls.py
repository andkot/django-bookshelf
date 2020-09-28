from django.contrib import admin
from django.urls import path
from .views import home_page, ListOfBooksView, ListOfBooksRestView

urlpatterns = [
    path('', ListOfBooksView.as_view(), name='home page'),
    path('books/', ListOfBooksRestView.as_view())
]
