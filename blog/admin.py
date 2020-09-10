from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import Post, Category, Product, Order  #Comment

import csv
from django.http import HttpResponse

class PostAdmin(admin.ModelAdmin):
    list_display = (
            'title',
            'hits',
            'call',
            )
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'price',
            'inventory',
            'call',
            'sum_call',
            'stat_rate',
            )
    pass


class OrderAdmin(admin.ModelAdmin):
    list_display = (
            'created_on',
            'sender',
            'author',
            'post',
            'quantity',
            'email',
            'phone',
            'message_store',
            'signature',
            )
    search_fields = ('sender', 'author', 'email', 'phone')
    actions = ["export_as_csv"]
 
    def export_as_csv(self, request, queryset):
 
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
        pass
    export_as_csv.short_description = "Export Selected"


#class CommentAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
#admin.site.register(Comment, CommentAdmin)
# Register your models here.
