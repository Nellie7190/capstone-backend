# from django.http.response import JsonResponse
# from django.shortcuts import render
# from rest_framework import permissions
# from capBackend import serializers
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User, Review, Place
from .serializers import PlaceSerializer, ReviewSerializer, UserSerializer

# Create your views here.
class PlaceList(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'capBackend/user_list.html', {'users': users})

# def place_list(request):
#     places = Place.objects.all().values('id', 'name', 'address', 'isBlackOwned', 'isWomanOwned', 'isENMOwned', 'isLComOwned', 'allowsPets', 'hoursOpen')
#     places_list = list(places)
#     return JsonResponse(places_list, safe=False)

# def review_list(request):
#     reviews = Review.objects.all().values('id', 'isBlackOwned', 'isWomanOwned', 'isLComOwned', 'isENMOwned', 'allowsPets', 'hoursOpen', 'rating', 'comment')
#     reviews_list = list(reviews)
#     return JsonResponse(reviews_list, safe=False)

# def user_detail(request, pk):
#     user = User.objects.get(id=pk)
#     return render(request, 'capBackend/user_detail.html', {'user': user})

# def place_detail(request, pk):
#     place = Place.objects.get(id=pk)
#     return render(request, 'capBackend/place_detail.html', {'place': place})

# def review_detail(request, pk):
#     review = Review.objects.get(id=pk)
#     return render(request, 'capBackend/review_detail.html', {'review': review})    