# Generated by Django 3.0.8 on 2020-07-30 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='call',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
