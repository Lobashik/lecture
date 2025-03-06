from rest_framework.serializers import ModelSerializer, ValidationError

from .models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        exclude = ('id', )
    
    def validate_name(self, value):
        if len(value) < 5:
            raise ValidationError('Name is too short')
        return value