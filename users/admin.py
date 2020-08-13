from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(admin.ModelAdmin):
    list_display = (
            'user_id',
            'name',
            'dob',
            'email',
            'phone',
            'address',
            'level',
            )
    search_fields = ('user_id', 'name', 'email')


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

 #Deletes Admin's Group
# Register your models here.
