from django.db import models
from category.models import Category 
class Product(models.Model):
    name=models.CharField(max_length=30,unique=True)
    price=models.IntegerField()
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    

