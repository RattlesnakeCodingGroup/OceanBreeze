from django.db import models

PER= [('1 lb', '1 lb'), ('1 dz','1 dz')]

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    measurement = models.CharField(max_length=20, choices=PER)
    quantity = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.title