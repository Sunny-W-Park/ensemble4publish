from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from django.utils import timezone

class Press(models.Model):
    created_on = models.DateTimeField()
    source = models.CharField(max_length = 255, verbose_name = '출처')
    title = models.CharField(max_length = 255, verbose_name = '기사제목')
    href = models.CharField(max_length = 2550, verbose_name = '바로가기링크')

# Create your models here.
