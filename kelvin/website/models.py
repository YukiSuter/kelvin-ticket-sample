from django.db import models

class Order(models.Model):
    name=models.CharField(max_length=100, primary_key=True)
    email=models.CharField(max_length=100)
    concession=models.BooleanField(default=False)
    ticket_sent=models.BooleanField(default=False)
    ticket_validity=models.BooleanField(default=True)
    ticket_code=models.CharField(max_length=12)
    purchase_id=models.CharField(max_length=100)
    concert_number=models.CharField(max_length=1, default=0)

# Create your models here.
