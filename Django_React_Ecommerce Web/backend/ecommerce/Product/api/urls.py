from django.urls import path
from .views import ProductListView, ProductDetialView,AddToCart,OrderDetailView,EmptyCart

urlpatterns = [

    path('', ProductListView.as_view()),
    path('<pk>', ProductDetialView .as_view()),
    path('addCart/', AddToCart.as_view()),
    path('fetchCart/', OrderDetailView.as_view()),
    path('EmptyCart/', EmptyCart.as_view()),

]