# Generated by Django 3.2.6 on 2021-10-07 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
