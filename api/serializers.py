from rest_framework import serializers

from restaurants.models import (
	Restaurant,
	Day,
	OperatingTime,
	Category,
	Item,
	Queue
)

from django.contrib.auth.models import User

class QueueListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Queue
		fields = '__all__'

class OperatingTimeListSerializer(serializers.ModelSerializer):
	class Meta:
		model = OperatingTime
		fields = '__all__'

class RestaurantListSerializer(serializers.ModelSerializer):
	
	queue = QueueListSerializer(many = True)
	operatingtime = OperatingTimeListSerializer(many = True)


	class Meta:
		model = Restaurant
		fields = '__all__'

	def get_queue(self, obj):
		return obj.queue_set.all()

	def get_operatingtime(self, obj):
		return obj.operatingtime_set.all()

class CategoryListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

class ItemListSerializer(serializers.ModelSerializer):
	category = CategoryListSerializer()
	class Meta:
		model = Item
		fields = '__all__'

	def get_category(self, obj):
		return obj.category_set.all()

class RestaurantDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = '__all__'



class QueueCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Queue
		exclude = ['position',]


	def create(self, validated_data):
		restaurant = validated_data['restaurant']
		user = validated_data['user']
		enter_q = Queue(restaurant= restaurant, user = user)
		enter_q.increment_position()
		enter_q.save()
		return validated_data

class QueueListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Queue
		fields ='__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, email= email, first_name = first_name, last_name = last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        my_username = data.get('username')
        my_password = data.get('password')

        try:
            user_obj = User.objects.get(username=my_username)
        except:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password")

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)

        data["token"] = token

        return data
        return data


