from django.contrib import admin
from daemun.models import Page

class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)
# Register your models here.
