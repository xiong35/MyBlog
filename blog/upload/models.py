import time
from django.db import models
import hashlib

# Create your models here.


class ImageTag(models.Model):
    tag_name = models.CharField(max_length=7)

    def __str__(self):
        return self.tag_name


def hashed_image_path(instance, filename):
    name, suffix = filename.split('.')
    sha1 = hashlib.sha1()
    sha1.update(name.encode('utf-8'))
    hashed = sha1.hexdigest()
    year_month_day_ = time.strftime("%Y/%m/%d/", time.localtime())
    return year_month_day_+hashed+'.'+suffix


class ImageBed(models.Model):
    image_path = models.ImageField(upload_to=hashed_image_path)
    origin_name = models.CharField(max_length=20)

    def __str__(self):
        return self.origin_name


class MyImage(models.Model):
    image_path = models.ImageField(upload_to=hashed_image_path)
    origin_name = models.CharField(max_length=20)
    tags = models.ManyToManyField(ImageTag)
    # 1: mid school
    # 2: high school
    # 4: college
    # 8: undefined
    # 16: undefined
    # 32: undefined
    authority = models.CharField(max_length=4, default='075')

    class Meta:
        ordering = ['image_path']

    def __str__(self):
        return self.origin_name
