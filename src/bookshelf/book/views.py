from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer

def home_page(request):
    return render(request, 'home_page.html')

class ListOfBooksView(ListView):
    model = Book
    template_name = 'home_page.html'

class ListOfBooksRestView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data})



