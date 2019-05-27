from django.db import models
from django.contrib.auth.models import User

##change it to incorporate more than preselected types
class RestaurantType(models.Model):
	RESTAURANT_TYPES = (
		('Japanese', 'Japanese'),
		('Italian', 'Italian' ),
		('Mexican', 'Mexican')
	)
	restaurant = models.CharField(max_length=20, choices = RESTAURANT_TYPES)

	def __str__(self):
		return self.restaurant


class Restaurant(models.Model):
	name = models.CharField(max_length = 100)
	picture = models.ImageField(null = True, blank = True)
	description = models.TextField()
	foodtype = models.ForeignKey(RestaurantType, on_delete = models.CASCADE, related_name = 'foodtype')

	def __str__(self):
		return self.name

class RestaurantUser(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete= models.CASCADE, null=True,blank =True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Day(models.Model):
	DAY_CHOICES = (
		('Sa' , 'Saturday'),
		('Su' , 'Sunday'),
		('Mo' , 'Monday'),
		('Tu' , 'Tuesday'),
		('We' , 'Wednesday'),
		('Th' , 'Thursday'),
		('Fr', 'Friday')
	)
	day = models.CharField(max_length=2, choices = DAY_CHOICES)

	def __str__(self):
		return self.day

class OperatingTime(models.Model):
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	day = models.ManyToManyField(Day)
	restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name ='operatingtime')

class Category(models.Model):
	MENU_TYPES = (
		('Breakfast', 'Breakfast'),
		('Lunch' , 'Lunch'),
		('Dinner' , 'Dinner'),
		('Brunch' , 'Brunch'),
		('Dessert', 'Dessert')
	)

	restaurant = models.ForeignKey(Restaurant, on_delete= models.CASCADE, related_name= 'category')
	name = models.CharField(max_length = 20, choices = MENU_TYPES)

	def __str__(self):
		return self.name + " " + self.restaurant.name

class Item(models.Model):
	name = models.CharField(max_length = 100)
	picture = models.ImageField(null = True, blank = True)
	description = models.TextField()
	price = models.DecimalField(max_digits = 5, decimal_places = 3)
	category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'item')

	def __str__(self):
		return self.name

class Queue(models.Model):
	position = models.IntegerField()
	user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
	restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name = 'queue')
	guests = models.IntegerField()

	class Meta:
		unique_together =(('position', 'restaurant'),
			('restaurant', 'user'))

		ordering = ['-position']

	def increment_position(self):
		q = Queue.objects.filter(restaurant = self.restaurant)

		if q:
			self.position = q.first().position + 1
		else:
			self.position = 1
		
