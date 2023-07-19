from django.db import models
from app.models import Category

class Product(models.Model):
    product_name = models.CharField(max_length=50, null=True)
    marque = models.CharField(max_length=50, null=True)
    performance = models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.marque 
    