from rest_framework import serializers
from base.models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class BookListSerializer(serializers.ModelSerializer):
    #average_raiting = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['title', 'genre', 'author', 'reviews']
        depth = 1
        
class BookSerializer(serializers.ModelSerializer):
    #average_raiting = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['title', 'genre', 'author', 'description', 'published_date', 'reviews', 'in_favourites']
        depth = 1


    # reviews = serializers.StringRelatedField(many=True)
    # reviews = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='raiting'
    # )
    #average_raiting = 5#ReviewSerializer(many=True, read_only=True)

    # def get_reviews(self, obj):
    #     reviews = Review.objects.filter(book=self.context['request'].book_id,book=obj)
    #     return ReviewSerializer(reviews, many=True).data


class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = '__all__'
