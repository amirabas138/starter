from django.contrib import admin
from .models import *
class userAdmin(admin.ModelAdmin):
    list_display=('email','username','is_active','is_admin')
    list_filter=('is_admin','is_active')
    search_fields=("username","email")
    prepopulated_fields={'username':('email',)}
    ordering=['is_admin']
# Register your models here.
admin.site.register(MyUser,userAdmin)
admin.site.register(Post)