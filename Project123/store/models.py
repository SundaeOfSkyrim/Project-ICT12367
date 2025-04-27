from django.db import models

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='shoes/')

    def __str__(self):
        return self.name

class Favorite(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

class Cart(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)