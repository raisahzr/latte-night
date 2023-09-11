from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

    def check_stock(self):
        if self.amount > 0:
            return f"Stock of {self.name} is {self.amount}!"
        else:
            return f"Stock of {self.name} is not available."