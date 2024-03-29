# Generated by Django 3.0.8 on 2020-07-17 03:37

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=17, unique=True, verbose_name='ID')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('dob', models.DateField(max_length=10, null=True, verbose_name='Date_of_Birth')),
                ('email', models.EmailField(max_length=128, null=True, unique=True, verbose_name='Email')),
                ('phone', models.IntegerField(null=True, unique=True, verbose_name='Phone')),
                ('name', models.CharField(max_length=17, null=True, verbose_name='Full Name')),
                ('address', models.CharField(max_length=128, null=True, verbose_name='Home Address')),
                ('level', models.CharField(default=3, max_length=17, verbose_name='level')),
                ('auth', models.CharField(max_length=10, null=True, verbose_name='Auth Code')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'User_List',
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
