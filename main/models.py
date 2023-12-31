from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def check_stock(self):
        if self.amount > 0:
            return f"Stock of {self.name} is {self.amount}!"
        else:
            return f"Stock of {self.name} is not available."
    
    def checkout(self):
        if self.category == "coffee":
            return f"Your order is {self.name} with Arabica coffee in total Rp{self.price}."
        else:
            return f"Your order is {self.name} in total Rp{self.price}."