from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.TextField()
    coffee_bean = models.TextField()

    def check_stock(self):
        if self.amount > 0:
            return f"Stock of {self.name} is {self.amount}!"
        else:
            return f"Stock of {self.name} is not available."
    
    def checkout(self):
        if self.category == "coffee":
            return f"Your order is {self.name} with {self.coffee_bean} coffee in total Rp{self.price}."
        else:
            return f"Your order is {self.name} in total Rp{self.price}."