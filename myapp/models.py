from django.db import models

# # Create your models here.
# # model for checkout page.


class Checkout(models.Model):
    country = models.CharField(max_length=20)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    companyname = models.CharField(max_length=20, blank=True, null=True)  # use blank=True, null=True instead of required=False
    address = models.CharField(max_length=50)
    state_or_province = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    order_notes = models.CharField(max_length=500, blank=True, null=True)  # increase max_length and use blank=True, null=True instead of required=False
    coupon_code = models.CharField(max_length=20, blank=True, null=True)

# # def for showing in shell the database instance in a string way of this my_checkout model
#     def __str__(self):
#         return f"{self.fname}{self.lname} lives in {self.Country}."

# # filter is for getting specific results 
# # Q is for capturing more complex results