# Generated by Django 2.2.12 on 2020-05-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0002_auto_20200512_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trap',
            name='context',
            field=models.CharField(default='计算机相关问题', max_length=50),
        ),
        migrations.AlterField(
            model_name='trap',
            name='solution',
            field=models.TextField(default='我想到了一个绝妙的解决方法, 但是这里位置太小, 我写不下...', max_length=1000),
        ),
    ]