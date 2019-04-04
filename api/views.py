from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	CreateAPIView,
	DestroyAPIView,

)
from rest_framework.views import APIView

from .serializers import (
	UserCreateSerializer, 
	UserLoginSerializer,  
)

from .serializers import (
	RestaurantListSerializer,
	QueueCreateSerializer,
	OperatingTimeListSerializer,
	ItemListSerializer,
	RestaurantDetailSerializer,
	QueueListSerializer
	
)
from restaurants.models import (
	Restaurant,
	Queue,
	OperatingTime,
	Item

)
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import Http404

class RestraurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer

class RestaurauntDetailView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'

class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class= ItemListSerializer


class OperatingTimeListView(ListAPIView):
	queryset = OperatingTime.objects.all()
	serializer_class = OperatingTimeListSerializer

class QueueView(APIView):
	def post(self, request):
		obj = request.data
		user = User.objects.get(id = obj['user'])
		restaurant = Restaurant.objects.get(id = obj['restaurant'])
		queue_obj = Queue(user = user, restaurant = restaurant)
		queue_obj.increment_position()
		queue_obj.save()
		return Response(RestaurantListSerializer(restaurant).data)


	def delete(self, request, queue_id):
		obj = request.data
		queue = Queue.objects.get(id= queue_id)
		restaurant_queues = Queue.objects.filter(restaurant = queue.restaurant).order_by('position')
		restaurant = Restaurant.objects.get(id = queue.restaurant.id)
		pos = queue.position
		queue.delete()

		for q in range(0 , len(restaurant_queues)):
			if restaurant_queues[q].position > pos:
				restaurant_queues[q].position -= 1
				restaurant_queues[q].save()

		
		return Response(RestaurantListSerializer(restaurant).data)


class QueueRemovalView(DestroyAPIView):
	queryset = Queue.objects.all()
	serializer_class = QueueCreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'queue_id'

	def perform_destroy(self, instance):
		queues = Queue.objects.filter(restaurant = instance.restaurant).order_by('position')
		pos = instance.position
		instance.delete()

		for q in range(0 , len(queues)):
			if queues[q].position > pos:
				queues[q].position -= 1
				queues[q].save()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


