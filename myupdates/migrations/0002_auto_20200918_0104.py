# Generated by Django 3.1 on 2020-09-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myupdates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='image1',
            field=models.ImageField(blank=True, max_length=550, null=True, upload_to='myupdates/images'),
        ),
    ]
