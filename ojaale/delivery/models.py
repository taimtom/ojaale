from django.db import models
from django.conf import settings
# Create your models here.
User=settings.AUTH_USER_MODEL

class DeliveryDetails(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField()
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    town=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    number=models.IntegerField()
    zip_code=models.IntegerField()
    comment=models.TextField(null=True, blank=True)
    paid=models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.first_name