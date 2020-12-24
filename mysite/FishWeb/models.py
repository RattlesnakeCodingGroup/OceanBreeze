from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.title