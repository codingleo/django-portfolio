from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    summary = models.TextField()
    intro_image = models.ImageField(upload_to="blog/")
    content = models.TextField()
    published = models.BooleanField(default=True)
    publish_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    
