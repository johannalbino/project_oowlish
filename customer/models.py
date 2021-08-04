from django.db import models


class Customers(models.Model):

    id = models.AutoField("ID", primary_key=True, auto_created=True)
    first_name = models.CharField("First Name", max_length=255)
    last_name = models.CharField("Last Name", max_length=255, null=True, blank=True)
    email = models.EmailField("Email")
    gender = models.CharField("Gender Customer", max_length=15, null=True, blank=True)
    company = models.CharField("Company", max_length=100)
    city = models.CharField("City", max_length=255)
    title = models.CharField("Title", max_length=255, null=True, blank=True)
    longitude = models.DecimalField("Longitude", max_digits=20, decimal_places=13)
    latitude = models.DecimalField("Longitude", max_digits=20, decimal_places=13)

    class Meta:
        db_table = 'oowlish_customers'
