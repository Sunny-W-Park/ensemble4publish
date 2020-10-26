from django.contrib import admin
from .models import Press

class PressAdmin(admin.ModelAdmin):
    list_display = (
            'created_on',
            'source',
            'title',
            'href',
            )
    search_fields = ('source', 'title')
    pass

admin.site.register(Press, PressAdmin)


# Register your models here.
