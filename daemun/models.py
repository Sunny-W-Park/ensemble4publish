from django.db import models

class Page(models.Model):
    page_images = models.ImageField(upload_to = 'page/images', max_length = 550, null = True, blank = True)
    page_images2  = models.ImageField(upload_to = 'page/images', max_length = 550, null = True, blank = True)
    page_images3 = models.ImageField(upload_to = 'page/images', max_length = 550, null = True, blank = True)
    page_images4 = models.ImageField(upload_to = 'page/images', max_length = 550, null = True, blank = True)
    page_images5 = models.ImageField(upload_to = 'page/images', max_length = 550, null = True, blank = True)
    page_images6 = models.ImageField(upload_to = 'page/images', max_length = 550, null = True, blank = True)

# Create your models here.
