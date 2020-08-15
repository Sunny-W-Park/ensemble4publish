# Generated by Django 3.0.8 on 2020-08-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20200815_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image5',
            field=models.ImageField(blank=True, max_length=550, null=True, upload_to='blog/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='guide',
            field=models.TextField(max_length=2550, null=True),
        ),
    ]
