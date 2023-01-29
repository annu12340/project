from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='products')
    price = models.IntegerField()
    details = models.TextField()
    rating = models.CharField(max_length=10)
    count = models.IntegerField(default=452)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
