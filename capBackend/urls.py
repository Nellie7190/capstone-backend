from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlaceList.as_view(), name='place_list'),
    path('places/', views.PlaceList.as_view(), name='place_list'),
    path('places/<int:pk>', views.PlaceDetail.as_view(), name='place_detail'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
    # path('users/', views.UserList, name='user_list'),
    # path('users/<int:pk>', views.UserDetail, name='user_detail'),
]