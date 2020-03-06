from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from .utils import unique_slug_generator
# Create your models here.
from jobs.models import Job
User=get_user_model()

class ProfessionalQuerySet(models.QuerySet):
	def search(self,query=None,loc_query=None):
		qs=self
		if query is not None:
			look_up=(Q(name__icontains=query)|
					Q(profession__iexact=query)&
                    Q(location__iexact=loc_query))

			qs=qs.filter(look_up).distinct()
		return qs

class ProfessionalManager(models.Manager):
	def get_queryset(self):
		return ProfessionalQuerySet(self.model, using=self._db)

	def search(self,query=None):
		return self.get_queryset().search(query)
class Professional(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    profession=models.CharField(max_length=100)
    area_of_concentration=models.TextField(null=True,blank=True, help_text='seperate each with comma (,)')
    image=models.ImageField(upload_to='skill/image')
    cover=models.ImageField(upload_to='skill/cover')
    language=models.CharField(max_length=250)
    min_wage=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    ongoing_jobs=models.ManyToManyField(Job,blank=True)#, related_name='is_completed')
    details=models.TextField(null=True,blank=True, help_text='Type comma twice (,,) to add paragraph')
    skills=models.TextField(null=True,blank=True, help_text='seperate each with comma (,)')

    #school
    school=models.CharField(max_length=250,null=True,blank=True)
    start_end_date=models.CharField(max_length=250,null=True,blank=True)
    school_qualification=models.CharField(max_length=250,null=True,blank=True)
    #experience
    employer=models.CharField(max_length=250,null=True,blank=True)
    job_start_end_date=models.CharField(max_length=250,null=True,blank=True)
    job_description=models.CharField(max_length=250,null=True,blank=True)
    job_image=models.ImageField(upload_to='skill/cover')
    job_url=models.CharField(max_length=250,null=True,blank=True)
    #others
    facebook=models.CharField(max_length=250,null=True,blank=True)
    twitter=models.CharField(max_length=250,null=True,blank=True)
    linkdin=models.CharField(max_length=250,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(null=True, blank=True)

    #index
    top_ten=models.BooleanField(default=False)

    objects=ProfessionalManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("professional:detail", kwargs={'slug':self.slug})
    def get_details(self):
        return self.details.split(',,') 
    def get_skills(self):
        return self.skills.split(',') 
    def get_area_of_concentration(self):
        return self.area_of_concentration.split(',') 
    @property
    def get_content_type(self):
        instance=self
        content_type=ContentType.objects.get_for_model(instance.__class__)
        return content_type

    #def get_markdown(self):
    #	details=self.details
    #	markdown_text=markdown(details)
    #	return mark_safe(markdown_text)
    # @property
    # def get_content_type(self):
    #     instance=self
    #     content_type=ContentType.objects.get_for_model(instance.__class__)
    #     return content_type

    class Meta:
        ordering=["-timestamp"]



def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.name = instance.name.capitalize()
	if not instance.slug:
		instance.slug =unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Professional)





class Testimony(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)

    selected=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username