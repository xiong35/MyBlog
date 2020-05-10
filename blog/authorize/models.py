from django.db import models


class Question(models.Model):
    category = models.CharField(max_length=7, default='关于我')
    question = models.CharField(max_length=20)
    answer = models.CharField(max_length=10)

    def __str__(self):
        return self.question


class Visiter(models.Model):
    token = models.CharField(max_length=260)
    authority = models.CharField(max_length=4, default='070')
    expire = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.expire)

    class Meta:
        ordering = ["expire"]
