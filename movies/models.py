from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=100, verbose_name='Movie Title')
    description = models.TextField(verbose_name='Movie Description')
    image = models.CharField(max_length=50, verbose_name='Movie Image')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Upload Date')
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/' + self.image