# Generated by Django 2.2.12 on 2020-05-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorize', '0003_auto_20200510_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='visiter',
            name='expire',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
