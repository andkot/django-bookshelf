from django.contrib import admin
from django.urls import path, include
from .views import BooksOwners, BooksOwnerDetails

urlpatterns = [
    path('', BooksOwners.as_view(), name='books owner list'),
    path('<int:pk>', BooksOwnerDetails.as_view(), name='books owner')
]