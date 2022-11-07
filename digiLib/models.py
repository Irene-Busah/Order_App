from email.policy import default
from operator import mod
from django.db import models

# Create your models here.
PRODUCT_TYPE = (
    ("1", "Food"),
    ("2", "Clothes"),
    ("3", "Shoes"),
    ("4", "Cosmetics"),
    ("5", "Sandals"),
    ("6", "Bags"),
    ("7", "Accessories"),
    ("8", "Other")
)
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_type = models.CharField(
        max_length=50,
        choices = PRODUCT_TYPE,
        default = "1"
    )
    price = models.CharField(max_length=30)
    product_image = models.ImageField(upload_to='files/items')
    product_desc = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.product_name
