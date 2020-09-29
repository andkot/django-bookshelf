from rest_framework import serializers
from .models import BooksOwner

class BooksOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksOwner
        fields = '__all__'
