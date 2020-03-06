from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.db.models import Q

from .utils import unique_slug_generator

# Create your models here.
from lessor.models import Lessor
class PropertyQuerySet(models.QuerySet):
	def search(self,query=None):
		qs=self
		if query is not None:
			look_up=(Q(category__iexact=query)|
					Q(name__icontains=query))

			qs=qs.filter(look_up).distinct()
		return qs

class PropertyManager(models.Manager):
	def get_queryset(self):
		return PropertyQuerySet(self.model, using=self._db)

	def search(self,query=None):
		return self.get_queryset().search(query)
class Property(models.Model):
    lessor=models.ForeignKey(Lessor,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.IntegerField()
    per=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    description=models.TextField()
    images=models.ImageField(upload_to='properties/images',null=True,blank=True)
    videos=models.CharField(max_length=100,null=True,blank=True)
    additional_features=models.CharField(max_length=100, help_text='seperate each by Comma (,)')
    image=models.ImageField(upload_to='properties/image')
    quantity_available=models.CharField(max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=True,blank=True)

    objects=PropertyManager()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("properties:detail", kwargs={'slug':self.slug})
    def get_additional_features(self):
        return self.additional_features.split(',')

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.name = instance.name.capitalize()
	if not instance.slug:
		instance.slug =unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Property)