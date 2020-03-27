# Create your models here.
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

from product.models import Products

User=settings.AUTH_USER_MODEL


# Create your models here.
class WishManager(models.Manager):
	def toggle_product(self,request_product, username_to_toggle):
		wish_=Wish.objects.get(user__username__iexact=username_to_toggle)
		product=request_product
		in_wish=False
		if product in wish_.products.all():
			wish_.products.remove(product)
		else:
			wish_.products.add(product)
			in_wish=True
		return wish_,in_wish
class Wish(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	products=models.ManyToManyField(Products, related_name='in_Wish', blank=True)
	total=models.DecimalField(max_digits=100, decimal_places=2, default=0)

	objects=WishManager()


	def __str__(self):
		return self.user.username

def post_save_user_receiver(sender,instance,created,*args, **kwargs):


	if created:
		wish, is_created  = Wish.objects.get_or_create(user=instance)
		# default_user_profile = Wish.objects.get_or_create(user__id=1)[0]
		# default_user_profile.products.add(instance)
		# myprofile.followers.add(default_user_profile.user)
		# myprofile.followers.add(1)


post_save.connect(post_save_user_receiver, sender=User)

