from django.contrib import admin

from .models import ImageTag, ImageBed, MyImage


class ImageBedAdmin(admin.ModelAdmin):
    list_display = ('origin_name', 'image_path')


class MyImageAdmin(admin.ModelAdmin):
    list_display = ('origin_name', 'image_path')


class ImageTagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'count')


admin.site.register(ImageTag, ImageTagAdmin)
admin.site.register(ImageBed, ImageBedAdmin)
admin.site.register(MyImage, MyImageAdmin)
