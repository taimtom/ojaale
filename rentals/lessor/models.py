from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import unique_slug_generator
# Create your models here.
User=settings.AUTH_USER_MODEL
# Create your models here.
class Lessor(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='lessor/image/logo')
    cover_image=models.ImageField(upload_to='lessor/image/cover')
    phoneno=models.CharField(max_length=12)
    updated=models.DateTimeField(auto_now_add=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.company_name
    def get_lessor_url(self):
        return reverse("lessor:properties", kwargs={'slug':self.slug})
    def get_lessor_profile(self):
        return reverse("lessor:details", kwargs={'slug':self.slug})


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.name = instance.company_name.capitalize()
	if not instance.slug:
		instance.slug =unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Lessor)