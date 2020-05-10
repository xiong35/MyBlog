from django.contrib import admin

# Register your models here.
from .models import BlogMeta


class BlogMetaAdmin(admin.ModelAdmin):
    list_display = ('key', "value")


admin.site.register(BlogMeta, BlogMetaAdmin)
