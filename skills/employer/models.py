from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import unique_slug_generator
# Create your models here.


class EmployerQuerySet(models.QuerySet):
	def search(self,query=None):
		qs=self
		if query is not None:
			look_up=(Q(title__icontains=query)|
					Q(category__iexact=query)|
                    Q(location__iexact=query))

			qs=qs.filter(look_up).distinct()
		return qs

class EmployerManager(models.Manager):
	def get_queryset(self):
		return EmployerQuerySet(self.model, using=self._db)

	def search(self,query=None):
		return self.get_queryset().search(query)

User=get_user_model()
class Employer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100)
    company_tagline=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    description=models.TextField()
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='employers/images', null=True,blank=True)
    cover=models.ImageField(upload_to='employers/cover', null=True,blank=True)
    fax=models.CharField(max_length=100, null=True,blank=True)
    website=models.CharField(max_length=200, null=True,blank=True)
    facebook=models.CharField(max_length=200, null=True,blank=True)
    twitter=models.CharField(max_length=200, null=True,blank=True)
    linkedin=models.CharField(max_length=200, null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=True,blank=True)


    objects=EmployerManager()

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse("employer:detail", kwargs={'slug':self.slug})
    def get_bodytext(self):
        return self.description.split(',,') 

    #def get_markdown(self):
    #	bodytext=self.bodytext
    #	markdown_text=markdown(bodytext)
    #	return mark_safe(markdown_text)
    # @property
    # def get_content_type(self):
    #     instance=self
    #     content_type=ContentType.objects.get_for_model(instance.__class__)
    #     return content_type

    class Meta:
        ordering=["-timestamp"]



def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.company_name = instance.company_name.capitalize()
	if not instance.slug:
		instance.slug =unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Employer)






    





