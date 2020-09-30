from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    # title = serializers.CharField(max_length=255)
    # description = serializers.CharField()

    # def create(self, validated_data):
    #     return Book.objects.create(**validated_data)
