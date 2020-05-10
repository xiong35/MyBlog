from django.db import models


class BlogMeta(models.Model):
    key = models.CharField(max_length=12)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.key

    def update(self):
        self.value += 1
        self.save(update_fields=['value'])


