from django.db import models
#from product.models import Products
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import unique_slug_generator
# Create your models here.
User=settings.AUTH_USER_MODEL

class Company(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=11)
    logo=models.ImageField(upload_to='company/images', null=True, blank=True)
    cover=models.ImageField(upload_to='company/covers', null=True, blank=True)
    
    achievements=models.CharField(max_length=100,null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    #products=models.ManyToManyField(Products, related_name='our_products')
    location=models.TextField()
    product_cat=models.CharField(max_length=100)
    
    slug=models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    def get_company_url(self):
        return reverse("company:detail", kwargs={'slug':self.slug})

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.name = instance.name.capitalize()
	if not instance.slug:
		instance.slug =unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Company)


