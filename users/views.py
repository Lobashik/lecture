from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import *


class CreateBookAPIView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = BookSerializer


class ListBooksAPIView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = BookSerializer
    # queryset = Book.objects.filter(name__isnull=False)
    
    
    def get_queryset(self):
        return Book.objects.filter(name__contains=self.request.query_params.get('name'))
