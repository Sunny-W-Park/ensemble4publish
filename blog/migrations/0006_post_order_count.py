# Generated by Django 3.0.8 on 2020-08-02 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_order_이름'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='order_count',
            field=models.PositiveIntegerField(null=True, verbose_name='참여자 수'),
        ),
    ]
