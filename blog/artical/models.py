from django.db import models

# Create your models here.


class ArticalTag(models.Model):
    tag_name = models.CharField(max_length=7, default='未分类')

    def __str__(self):
        return self.tag_name


class Trap(models.Model):
    class Meta:
        ordering = ["last_update"]

    context = models.CharField(max_length=200, default='计算机相关问题',)
    problem = models.CharField(max_length=200, default='一个棘手的问题...')
    solution = models.CharField(
        max_length=700, default='我想到了一个绝妙的解决方法, 但是这里位置太小, 我写不下...')
    last_update = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(ArticalTag)

    def __str__(self):
        return self.problem


class Blog(models.Model):
    class Meta:
        ordering = ["last_update"]
    last_update = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=5000)
    headline = models.CharField(max_length=20)

    tags = models.ManyToManyField(ArticalTag)

    def __str__(self):
        return self.headline
