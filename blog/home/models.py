from django.db import models

# Create your models here.


class Statistic(models.Model):
    item = models.CharField(max_length=7)
    count = models.IntegerField(default='0')

    def __str__(self):
        return self.item
