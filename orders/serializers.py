from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'portfolio', 'symbol', 'quantity', 'order_type', 'price', 'created_at', 'status']