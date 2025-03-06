from django.urls import path

from .views import *


urlpatterns = [
    path('book/create/', CreateBookAPIView.as_view()),
    path('book/list/', ListBooksAPIView.as_view())
]