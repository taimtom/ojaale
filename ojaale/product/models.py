from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import unique_slug_generator
from company.models import Company

from reviews.models import Review

User=settings.AUTH_USER_MODEL

# Create your models here.
class Products(models.Model):
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100, null=True,blank=True )
    sub_category=models.CharField(max_length=100, null=True,blank=True )
    price=models.IntegerField()
    discounted_from=models.IntegerField(null=True,blank=True)
    availability=models.CharField(max_length=30)
    brand=models.CharField(max_length=100)
    size=models.CharField(max_length=100, null=True, blank=True)
    description=models.TextField()
    color=models.CharField(max_length=30,null=True, blank=True)
    image=models.ImageField(upload_to='product/images')
    timestamp=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=True, blank=True)

    class Meta:
      ordering=["-timestamp"]


    def __str__(self):
      return self.name
    
    def get_absolute_url(self):
      return reverse("products:detail", kwargs={'slug':self.slug})
    
    @property
    def get_content_type(self):
      instance=self
      content_type=ContentType.objects.get_for_model(instance.__class__)
      return content_type


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.name = instance.name.capitalize()
	if not instance.slug:
		instance.slug =unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Products)

