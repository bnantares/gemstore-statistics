from django.db import models
from django.views.generic import View
import sqlite3 as lite
import sys
# Create your models here.

class Sale(models.Model):
    customer = models.CharField(max_length=150)
    item = models.CharField(max_length=250)
    total = models.DecimalField(max_digits=5, decimal_places=0)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.customer}-{self.quantity}"