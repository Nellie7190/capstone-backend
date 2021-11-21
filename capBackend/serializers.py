from rest_framework import serializers
from .models import User, Review, Place

class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True,
    )
    user_url=serializers.ModelSerializer.serializer_url_field(view_name='user_detail')

    class Meta:
        model = User
        fields = ('id', 'userName', 'user_url', 'email', 'password', 'reviews')

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True,
    )
    place_url=serializers.ModelSerializer.serializer_url_field(view_name='place_detail')

    class Meta:
        model = Place
        fields = ('id', 'name', 'address', 'image', 'place_url', 'isBlackOwned', 'isWomanOwned', 'isENMOwned', 'isLComOwned', 'allowsPets', 'hoursOpen', 'reviews')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    place = serializers.HyperlinkedRelatedField(
        view_name='place_detail',
        read_only=True,
    )
    # user = serializers.HyperlinkedRelatedField(
    #     view_name='review_detail',
    #     read_only=True,
    # )
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True,
    )

    place_id=serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(),
        source='place'
    )
    
    user_id=serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )

    class Meta:
        model = Review
        fields = ('id', 'user', 'user_id', 'place', 'place_id', 'isBlackOwned', 'isWomanOwned', 'isLComOwned', 'isENMOwned', 'allowsPets', 'hoursOpen', 'rating', 'comment')
