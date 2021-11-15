from django.http import response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
import requests
from .serializers import BookSerializer, ExternalBookSerializer
from .models import Book


import logging
logging.basicConfig(level=logging.NOTSET)

# Create your views here.

# class BookView(APIView):
    
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response({'status_code': 200, 'status': 'success', 'data': serializer.data}, status = status.HTTP_200_OK)

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'status_code': 200,
            'status': 'success',
            'data': response.data
        }, status = status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        response =  super().retrieve(request, *args, **kwargs)
        return Response({
            'status_code': 200,
            'status': 'success',
            'data': response.data
        }, status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status_code': 201,
            'status': 'success',
            'data': [{'book': response.data}]
        }, status = status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        book_name = instance.name
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response({
            'status_code': 200,
            'status': 'success',
            'message': f'The book {book_name} was updated successfully',
            'data': serializer.data
        }, status = status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        book_name = instance.name
        self.perform_destroy(instance)
        return Response({
            'status_code': 200,
            'status': 'success',
            'message': f'The book {book_name} was deleted successfully',
            'data': []
        }, status = status.HTTP_200_OK)

class ExternalBookView(APIView):
    
    def get(self, request):
        book_name = request.GET.get('name', None)
        response_data = []
        if book_name:
            endpoint_url = 'https://www.anapioficeandfire.com/api/books'
            filter_params = {'name': book_name}
            external_books = requests.get(endpoint_url, params=filter_params).json()
            response_data = ExternalBookSerializer(external_books, many=True).data
        return Response({'status_code': 200, 'status': 'success', 'data': response_data}, status = status.HTTP_200_OK)

