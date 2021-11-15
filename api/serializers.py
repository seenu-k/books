from rest_framework import serializers
from datetime import datetime
from .models import Book

class StringArrayField(serializers.CharField):
    def to_representation(self, value):
        return value.split(",") if isinstance(value, str) else value

    def to_internal_value(self, data):
        data = ",".join([str(element) for element in data])
        return super().to_internal_value(data)

class BookSerializer(serializers.ModelSerializer):
    authors = StringArrayField()

    class Meta:
        model = Book
        fields = ('__all__')

class ExternalBookSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'name': instance['name'],
            'isbn': instance['isbn'],
            'authors': instance['authors'],
            'country': instance['country'],
            'number_of_pages': instance['numberOfPages'],
            'publisher': instance['publisher'],
            'release_date': datetime.fromisoformat(instance['released']).strftime('%Y-%m-%d')
        }