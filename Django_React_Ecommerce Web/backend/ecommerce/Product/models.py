from django.db import models
from accounts.models import UserAccount

# Create your models here.
class Products(models.Model):
    Product_Id = models.AutoField
    title = models.CharField(max_length= 120)
    Description= models.TextField()
    price = models.IntegerField()
    slug = models.SlugField()
    Product_Image = models.ImageField(upload_to='shop/images', default="")


    def __str__(self):
        return self.title


     
    

class Order(models.Model):
   Customer_Id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
   item = models.ForeignKey(Products, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)

   def __str__(self):
        return f"{self.quantity} of {self.item.title}"

   def get_item_price(self):
        return self.quantity * self.item.price

 


class OrderItem(models.Model):
    Customer_Id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    items = models.ManyToManyField(Order)


    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()



    

    
    
        
