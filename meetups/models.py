from distutils.command.upload import upload
from itertools import count
from pydoc import describe
from django.db import models

# Create your models here.


class meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    # python -m pip install pillow

    def __str__(self):
        return f'{self.title} - {self.slug}'
