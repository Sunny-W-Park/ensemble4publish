from django.contrib import admin
from team.models import Category, Press

class PressAdmin(admin.ModelAdmin):
    list_display = (
            'created_on',
            'source',
            'title',
            'href',
            )
    search_fields = ('source', 'title')
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Press, PressAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
