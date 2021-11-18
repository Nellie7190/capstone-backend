from rest_framework import serializers
from .models import User, Review, Place

# class UserSerializer(serialzers.HyperlinkedModelSerializer):
#     reviews = serializers.HyperlinkedRelatedField(
#         view_name='review_detail',
#         many=True,
#         read_only=True,
#     )

#     class Meta:
#         model = User
#         fields = ('userName', 'email', 'password')

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True,
    )
    place_url=serializers.ModelSerializer.serializer_url_field(view_name='place_detail')

    class Meta:
        model = Place
        fields = ('id', 'reviews', 'place_url', 'name', 'address', 'isBlackOwned', 'isWomanOwned', 'isENMOwned', 'isLComOwned', 'allowsPets', 'hoursOpen')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    place = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        read_only=True,
    )
    place_id=serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(),
        source='place'
    )

    class Meta:
        model = Review
        fields = ('id', 'place_id', 'place', 'isBlackOwned', 'isWomanOwned', 'isLComOwned', 'isENMOwned', 'allowsPets', 'hoursOpen', 'rating', 'comment')
