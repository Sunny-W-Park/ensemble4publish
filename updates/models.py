from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from django.db.models import Count
from django.utils import timezone

from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Feed(models.Model):
    created_on = models.DateTimeField('date published')
    categories = models.ManyToManyField('Category', related_name = 'feeds')
    title = models.CharField(max_length=255, verbose_name = '제목')
    call = models.PositiveIntegerField(default=0, verbose_name = '참여자수', null = True)
    maxinv = models.PositiveIntegerField(default=0, verbose_name = '인원', null = True)
    body = models.TextField()
    image1 = models.ImageField(upload_to = 'updates/images', max_length = 550, null = True, blank = True)
    def __str__(self):
        return self.title

class RSVP(models.Model):
    feed  = models.ForeignKey('Feed', on_delete=models.CASCADE, related_name='rsvp',  null = True) #forDB 
    sender = models.CharField(max_length = 60, null = True)
    email = models.CharField(max_length = 60, null = True, blank = False)
    phone = models.CharField(max_length = 120, null = False, blank = False)
    created_on = models.DateTimeField(auto_now_add = True, null = True)

# Create your models here.
