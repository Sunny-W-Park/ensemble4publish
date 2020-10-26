# Generated by Django 3.1 on 2020-10-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField()),
                ('source', models.CharField(max_length=255, verbose_name='출처')),
                ('title', models.CharField(max_length=255, verbose_name='기사제목')),
                ('href', models.CharField(max_length=2550, verbose_name='바로가기링크')),
            ],
        ),
    ]
