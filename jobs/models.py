from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image_intro = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'job'
        managed = True
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'