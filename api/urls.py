from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import (
	RestraurantListView,
	RestaurauntDetailView,
	QueueView,
	OperatingTimeListView,
	ItemListView,
	UserCreateAPIView
)

urlpatterns = [
	path('restaurant/list/', RestraurantListView.as_view(), name= 'rest-list'),
	path('queue/create/', QueueView.as_view(), name = 'queue-create'),
	path('queue/delete/<int:queue_id>/', QueueView.as_view(), name = 'queue-delete'),
	path('operating/', OperatingTimeListView.as_view(), name = 'operating-list'),
	path('item/list/', ItemListView.as_view(), name = 'item-list'),
	path('restaurant/detail/<int:restaurant_id>/', RestaurauntDetailView.as_view(), name = 'restaurant-detail'),
	path('signup/', UserCreateAPIView.as_view(), name="signup"),
    path('signin/',obtain_jwt_token, name="signin"),
    ]