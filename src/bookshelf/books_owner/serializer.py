from rest_framework import serializers
from .models import BooksOwner

class BooksOwnerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    username = serializers.EmailField(required=False)
    first_name = serializers.EmailField(required=False)
    last_name = serializers.EmailField(required=False)
    class Meta:
        model = BooksOwner
        fields = '__all__'
