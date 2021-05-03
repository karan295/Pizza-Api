  
__author__ = 'Karan Dey'
from rest_framework import serializers
from pizza_app.models import PizzaToppings,Pizza




class PizzaToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PizzaToppings
        fields=('Name',)





class PizzaSerializer(serializers.ModelSerializer):
    Pizza_toppings=PizzaToppingsSerializer(many=True)
    class Meta:
        model=Pizza
        fields=['Pizza_type','Pizza_toppings','Pizza_Size']



class PizzaListSerializer(serializers.ModelSerializer):
    Pizza_toppings=PizzaToppingsSerializer(many=True)
    class Meta:
        model=Pizza
        fields=['Pizza_type','Pizza_toppings','Pizza_Size','UpdateBy','createdBy','createdAt']

