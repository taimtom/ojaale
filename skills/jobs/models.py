from django.db import models

from employer.models import Employer
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import unique_slug_generator
# Create your models here.


class JobQuerySet(models.QuerySet):
	def search(self,query=None):
		qs=self
		if query is not None:
			look_up=(Q(title__icontains=query)|
					Q(category__iexact=query)|
                    Q(location__iexact=query))

			qs=qs.filter(look_up).distinct()
		return qs

class JobManager(models.Manager):
	def get_queryset(self):
		return JobQuerySet(self.model, using=self._db)

	def search(self,query=None):
		return self.get_queryset().search(query)
# Create your models here.
class Job(models.Model):
    employer=models.ForeignKey(Employer, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField(help_text='Type comma twice (,,) to add paragraph')
    category=models.CharField(max_length=200)
    image=models.ImageField(upload_to='job/image', null=True,blank=True)
    gender=models.CharField(max_length=200, null=True,blank=True)
    experience=models.CharField(max_length=200, null=True,blank=True)
    job_type=models.CharField(max_length=200, null=True,blank=True)
    requirement=models.TextField(help_text='separate each by comma (,)', null=True,blank=True)
    features=models.CharField(max_length=400,help_text='separate each with comma (,)', null=True,blank=True)
    max_wage=models.CharField(max_length=200, null=True,blank=True)
    min_wage=models.CharField(max_length=200, null=True,blank=True)
    wages=models.CharField(max_length=200, null=True,blank=True)
    job_time=models.CharField(max_length=200, null=True,blank=True)
    location=models.CharField(max_length=200, null=True,blank=True)
    thumbnail=models.CharField(max_length=200, null=True,blank=True)
    completed=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=True,blank=True)

    objects=JobManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:detail", kwargs={'slug':self.slug})
    def get_bodytext(self):
        return self.description.split(',,') 

    #def get_markdown(self):
    #	bodytext=self.bodytext2
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
	instance.title = instance.title.capitalize()
	if not instance.slug:
		instance.slug =unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Job)