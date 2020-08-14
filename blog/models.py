from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from django.db.models import Count
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT

#Signals
#from django.db.models.signals import post_save
#from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name = '제목')
    hits = models.PositiveIntegerField(verbose_name = '조회수', default = 0)
    totalfund = models.CharField(max_length=20, null = True, blank = True)
    call = models.PositiveIntegerField(default=0, verbose_name = '주문량', null = True) 
    call_rate = models.PositiveIntegerField(default=0, verbose_name = '쿠폰펀딩률', null = True)
    menu = models.TextField(max_length=255, verbose_name = '메뉴', null = True)
    price = models.IntegerField(default=0, verbose_name = '정가', null = True)
    discounted = models.IntegerField(default=0, verbose_name = '할인가', null = True)
    min_call = models.PositiveIntegerField(default=0, verbose_name = '최소판매량', null = True)
    target_call = models.PositiveIntegerField(default=0, verbose_name = '목표판매량',  null = True)
    max_call = models.PositiveIntegerField(default=0, verbose_name= '최대판매량',  null = True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    price_details = models.TextField(max_length=2550, null = True)
    message_owner = models.TextField(max_length=255, null = True)
    store_info = models.TextField(max_length=255, null = True)
    guide = models.TextField(max_length=255, null = True)
    image1 = models.ImageField(upload_to ='blog/images', max_length = 550, null = True, blank = True)
    image2 = models.ImageField(upload_to ='blog/images', max_length = 550, null = True, blank = True)
    image3 = models.ImageField(upload_to ='blog/images', max_length = 550, null = True, blank = True)
    image4 = models.ImageField(upload_to ='blog/images', max_length = 550, null = True, blank = True)
    image5 = models.ImageField(upload_to ='blog/images', max_length = 550, null = True, blank = True)
    def __str__(self):
        return self.title

    @property
    def click(self):
        self.hits += 1
        self.save()

class Product(models.Model):
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    def price_display(self):
        return "₩%s" % self.price
    inventory = models.IntegerField(default = 0)
    call = models.IntegerField(default = 0)
    sum_call = models.IntegerField(default = 0)
    stat_rate = models.IntegerField(default = 0)

class Order(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='orders',  null = True) #forDB 
    sender = models.CharField(max_length = 60, null = True)
    author = models.CharField(max_length = 60, null = True, blank = True)
    quantity = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    email = models.CharField(max_length = 60, null = True, blank = False)
    phone = models.CharField(max_length = 120, null = False, blank = False)
    message_store = models.CharField(max_length=256, null = True, blank = True)
    created_on = models.DateTimeField(auto_now_add = True, null = True)
    def __str__(self):
        return self.author


class Hitcount(models.Model, HitCountMixin):
    hit_count_generic = GenericRelation(
            MODEL_HITCOUNT, object_id_field='object_pk',
            related_query_name='hit_count_generic_relation'
            )
    pass

#class Comment(models.Model):
#    author = models.CharField(max_length=60)
#    body = models.TextField()
#    created_on = models.DateTimeField(auto_now_add=True)
#    post = models.ForeignKey('Post', on_delete=models.CASCADE)
#    def __str__(self):
#        return self.body

# Create your models here.
