from rest_framework import serializers
from testapp.models import *


class PizzaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=pizza_type
        fields='__all__'

class PizzaSizeSeriaizer(serializers.ModelSerializer):
    class Meta:
        model=pizza_size
        fields='__all__'

class PizzaToppingsSeriaizer(serializers.ModelSerializer):
    class Meta:
        model=pizza_toppings
        fields='__all__'


class PizzaOrdersSerializer(serializers.ModelSerializer):
    pizza_toppings=serializers.JSONField()
    class Meta:
        model=pizza_orders
        fields='__all__'
