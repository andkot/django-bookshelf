from django.contrib import admin
from django.urls import path, include
from .views import BooksOwnersAPIView

urlpatterns = [
    path('', BooksOwnersAPIView.as_view(), name='books owner list')
]