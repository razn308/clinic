from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

# Create your models here.
class BlogPost(models.Model):
    Category = (
        ('Mental Health',' Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19','Covid19'),
        ('Immunization','Immunization'),
    )
    title = models.CharField(max_length=250, null=False, blank=False)
    category = models.CharField(max_length=13, choices=Category, default=None)
    content = models.TextField(max_length=50000, null=False, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to = "images/" )
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")    
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    summary =  models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title + " | " + str(self.author)


@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_blog_post_receiver(sender, instance,**kwargs):
    if not instance.summary:
        instance.summary = slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)
