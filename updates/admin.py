from django.contrib import admin
from django.utils.safestring import mark_safe
from updates.models import Category, Feed, RSVP

class CategoryAdmin(admin.ModelAdmin):
    pass

class FeedAdmin(admin.ModelAdmin):
    pass

class RSVPAdmin(admin.ModelAdmin):
    list_display = (
            'sender',
            'email',
            'phone',
            )
    pass

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(RSVP, RSVPAdmin)
