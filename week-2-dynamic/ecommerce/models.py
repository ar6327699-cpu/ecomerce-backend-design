from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    image = models.URLField(max_length=500, default="https://via.placeholder.com/150")
    description = models.TextField()
    stock = models.IntegerField(default=10)

    def __str__(self):
        return self.name