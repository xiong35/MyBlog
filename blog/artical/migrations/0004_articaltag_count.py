# Generated by Django 2.2.12 on 2020-04-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0003_auto_20200408_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='articaltag',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]