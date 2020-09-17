# Generated by Django 3.1 on 2020-09-16 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=60, null=True)),
                ('email', models.CharField(max_length=60, null=True)),
                ('phone', models.CharField(max_length=120)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('feed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rsvp', to='updates.feed')),
            ],
        ),
    ]
