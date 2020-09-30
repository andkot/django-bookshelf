from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BooksOwner
from .serializer import BooksOwnerSerializer


class BooksOwners(APIView):
    """
    List all books owners, or create a new books owner.
    """

    def get(self, request):
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


class BooksOwnerDetails(APIView):

    def get_books_owner(self, pk):
        try:
            return BooksOwner.objects.get(pk=pk)
        except BooksOwner.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """Return a books owner"""
        return Response(BooksOwnerSerializer(self.get_books_owner(pk)).data)

    def put(self, request, pk=None):
        """Edit Books owner"""
        books_owner = self.get_books_owner(pk)
        serializer = BooksOwnerSerializer(books_owner, data=request.data)
        if serializer.is_valid():
            books_owner.email = request.data['email']
            books_owner.username = request.data['username']
            serializer.save()
            return Response({'message': 'Books owner had been successfully updated!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        books_owner = self.get_books_owner(pk)
        books_owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
