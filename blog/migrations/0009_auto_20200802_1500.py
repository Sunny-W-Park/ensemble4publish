# Generated by Django 3.0.8 on 2020-08-02 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200802_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='blog.Post'),
        ),
    ]
