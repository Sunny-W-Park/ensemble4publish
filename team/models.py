from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Press(models.Model):
    created_on = models.DateTimeField()
    categories = models.ManyToManyField('Category', related_name = 'Presss')
    source = models.CharField(max_length = 255, verbose_name = '출처')
    title = models.CharField(max_length = 255, verbose_name = '기사제목')
    href = models.CharField(max_length = 2550, verbose_name = '바로가기링크')



# Create your models here.
