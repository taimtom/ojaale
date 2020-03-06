from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

User=settings.AUTH_USER_MODEL

class ReviewManager(models.Manager):
    def all(self):
        qs=super(ReviewManager,self).filter(parent=None)
        return qs
    def filter_by_instance(self, instance):
        content_type=ContentType.objects.get_for_model(instance.__class__)
        obj_id=instance.id
        qs=super(ReviewManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
        return qs
# Create your models here.
class Review(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type= models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id   =models.PositiveIntegerField()
    content_object= GenericForeignKey('content_type', 'object_id')
    content     =models.TextField()
    rating      = models.PositiveIntegerField()
    parent=models.ForeignKey("self", null=True, blank=True ,on_delete=models.CASCADE)
    timestamp   =models.DateTimeField(auto_now_add=True)

    objects=ReviewManager()

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return self.user.username
    
    def children(self):
        return Comment.objects.filter(parent=self)

    
    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True