from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import Post, Category, Product, Order  #Comment


class PostAdmin(admin.ModelAdmin):
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
    search_fields = ('author', 'post', 'phone')



#class CommentAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
#admin.site.register(Comment, CommentAdmin)
# Register your models here.
