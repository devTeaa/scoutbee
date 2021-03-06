from rest_framework import serializers
from dishes.models import Dish


# Dish Serializer


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
