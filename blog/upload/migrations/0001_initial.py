# Generated by Django 2.2.12 on 2020-04-08 20:09

from django.db import migrations, models
import upload.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.ImageField(upload_to=upload.models.hashed_image_path)),
                ('origin_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ImageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.ImageField(upload_to=upload.models.hashed_image_path)),
                ('origin_name', models.CharField(max_length=20)),
                ('authority', models.CharField(default='070', max_length=4)),
                ('tags', models.ManyToManyField(to='upload.ImageTag')),
            ],
            options={
                'ordering': ['image_path'],
            },
        ),
    ]
