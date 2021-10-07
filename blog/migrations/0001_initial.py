# Generated by Django 3.2.6 on 2021-10-07 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.datetime(2021, 10, 7, 11, 46, 33, 919158))),
                ('author', models.CharField(max_length=50)),
                ('img_author', models.ImageField(upload_to='')),
                ('img_blog', models.ImageField(upload_to='')),
                ('views', models.IntegerField()),
                ('body', models.TextField()),
            ],
        ),
    ]
