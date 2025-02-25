from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR')])


class Discount(models.Model):
    code = models.CharField(max_length=50, unique=True)


class Tax(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    jurisdiction = models.CharField(max_length=255, default='US')


class Order(models.Model):
    items = models.ManyToManyField(Item)
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR')])
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    tax = models.ForeignKey(Tax, null=True, blank=True, on_delete=models.SET_NULL)



