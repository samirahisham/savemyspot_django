from django.contrib import admin
from .models import (
	Restaurant, 
	OperatingTime,
	Day,
	Category,
	Item,
	Queue,
	RestaurantType
)



class CategoryAdmin(admin.ModelAdmin):
	list_display= ['_type', 'restaurant']

admin.site.register(Restaurant)
admin.site.register(OperatingTime)
admin.site.register(Day)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item)
admin.site.register(Queue)
admin.site.register(RestaurantType)





