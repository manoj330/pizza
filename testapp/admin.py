from django.contrib import admin
from testapp.models import *
# Register your models here.
admin.site.register(pizza_type)
admin.site.register(pizza_size)
admin.site.register(pizza_toppings)
admin.site.register(pizza_orders)