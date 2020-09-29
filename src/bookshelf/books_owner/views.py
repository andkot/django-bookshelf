from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BooksOwner
from .serializer import BooksOwnerSerializer


class BooksOwnersAPIView(APIView):
    """Return all books owners"""

    def get(self, request, formate=None):
        """Return list of all books owner"""
        return Response(BooksOwnerSerializer(BooksOwner.objects.all(), many=True).data)

    def post(self, request):
        """Create a new books owner"""
        serializer = BooksOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Books owner has been created'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Edit Books owner"""
        books_owner = BooksOwner.objects.get(pk=pk)
        serializer = BooksOwnerSerializer(books_owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Books owner had been successfully updated!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
