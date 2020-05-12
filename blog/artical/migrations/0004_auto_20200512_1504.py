# Generated by Django 2.2.12 on 2020-05-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0003_auto_20200512_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='headline',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='trap',
            name='context',
            field=models.CharField(default='计算机相关问题', max_length=70),
        ),
        migrations.AlterField(
            model_name='trap',
            name='problem',
            field=models.CharField(default='一个棘手的问题...', max_length=210),
        ),
        migrations.AlterField(
            model_name='trap',
            name='solution',
            field=models.TextField(default='我想到了一个绝妙的解决方法, 但是这里位置太小, 我写不下...', max_length=3000),
        ),
    ]
