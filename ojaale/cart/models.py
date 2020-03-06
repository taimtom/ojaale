from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

from product.models import Products

User=settings.AUTH_USER_MODEL


# Create your models here.
class CartManager(models.Manager):
	def toggle_product(self,request_product, username_to_toggle):
		cart_=Cart.objects.get(user__username__iexact=username_to_toggle)
		product=request_product
		in_cart=False
		if product in cart_.products.all():
			cart_.products.remove(product)
		else:
			cart_.products.add(product)
			in_cart=True
		return cart_,in_cart
class Cart(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	products=models.ManyToManyField(Products, related_name='in_cart', blank=True)
	total=models.DecimalField(max_digits=100, decimal_places=2, default=0)

	objects=CartManager()


	def __str__(self):
		return self.user.username

def post_save_user_receiver(sender,instance,created,*args, **kwargs):


	if created:
		cart, is_created  = Cart.objects.get_or_create(user=instance)
		# default_user_profile = Cart.objects.get_or_create(user__id=1)[0]
		# default_user_profile.products.add(instance)
		# myprofile.followers.add(default_user_profile.user)
		# myprofile.followers.add(1)


post_save.connect(post_save_user_receiver, sender=User)

