from rest_framework import serializers
from Product.models import Products,Order,OrderItem


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ProductSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('title', 'Description', 'price','Product_Image','slug')



class OrderSerializer(serializers.ModelSerializer):
    item = StringSerializer()
    item_obj = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = (
            'id',
            'item',
            'item_obj',
            'quantity',
            'total'
            
            
        )

    def get_item_obj(self, obj):
        return ProductSerialzer(obj.item).data

    def get_total(self, obj):
        return obj.get_item_price()
  
    

    

  


class OrderItemSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'order_items',
            'total',
            'coupon'
        )

    def get_order_items(self, obj):
        return OrderSerializer(obj.items.all(), many=True).data

    def get_total(self, obj):
        return obj.get_total()
