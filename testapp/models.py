from django.db import models

# Create your models here.
class pizza_type(models.Model):
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.type
class pizza_size(models.Model):
    size=models.CharField(max_length=100)
    def __str__(self):
        return self.size
class pizza_toppings(models.Model):
    toppings=models.CharField(max_length=100)
    
    

class pizza_orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    pizza_type=models.ForeignKey("pizza_type",on_delete=models.CASCADE)
    pizza_size=models.ForeignKey("pizza_size",on_delete=models.CASCADE)
    pizza_toppings=models.CharField(max_length=200)
    


