from basket.models import BasketItem
from rest_framework.serializers import ModelSerializer



class BasketItemSerializer(ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ['owner', 'course', 'basket', 'created_at']