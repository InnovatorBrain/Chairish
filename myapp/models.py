from django.db import models

# Create your models here.
# model for checkout page.


class my_checkout(models.Model):
    Country = models.CharField(max_length=20)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    companyname = models.CharField(max_length=20)
    address = models.TextField(max_length=50)
    state_country = models.CharField(max_length=20)
    postal_zip = models.IntegerField(max_length=10)
    email_address = models.EmailField()
    Phone = models.IntegerField()
    order_notes = models.TextField()
    Coupon_Code = models.CharField(max_length=20)
# def for showing in shell the database instance in a string way of this my_checkout model
    def __str__(self):
        return f"{self.fname}{self.lname} lives in {self.Country}."

# filter is for getting specific results 
# Q is for capturing more complex results