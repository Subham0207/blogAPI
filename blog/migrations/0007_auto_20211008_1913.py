# Generated by Django 3.2.6 on 2021-10-08 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 8, 19, 13, 7, 641519)),
        ),
    ]
