from rest_framework.generics import ListAPIView , RetrieveAPIView
from Product.models import Products, Order 
from .serialzers import ProductSerialzer , OrderSerializer ,OrderItemSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist


class ProductListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Products.objects.all()
    serializer_class = ProductSerialzer

class ProductDetialView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Products.objects.all()
    serializer_class = ProductSerialzer

class AddToCart(APIView):
    def post(self, request, *args, **kwargs):
        
        slug = request.data.get('slug', None)
        if slug is None:
            return Response({"message": "Invalid data"}, status=HTTP_400_BAD_REQUEST)
        item = get_object_or_404(Products, slug=slug)
        
        if Order.objects.filter(item_id=slug,Customer_Id_id=request.user.id).exists():
            # update quantity
            order = Order.objects.filter(item_id=slug,Customer_Id_id=request.user.id).get()
            order.quantity += 1
            order.save()
            
        else:
            # insert a data in a row
            Order.objects.create(item_id=slug,Customer_Id_id=request.user.id)

        
        
        return Response({"message": "successful"})

class EmptyCart(ListAPIView):
    def delete(self, request, *args, **kwargs):
        
        
        if Order.objects.filter(Customer_Id_id=request.user.id).exists():
            # empty cart
            order = Order.objects.filter(Customer_Id_id=request.user.id).delete()
            
           
   
        return Response({"message": "successful"})


class OrderDetailView(ListAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        uid= self.request.user.id
      
        try:
            order = Order.objects.filter(Customer_Id_id = uid)
            return order
        except ObjectDoesNotExist:
            return Response({"message": "Invalid data"}, status=HTTP_400_BAD_REQUEST)

            
