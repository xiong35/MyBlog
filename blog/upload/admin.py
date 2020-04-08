from django.contrib import admin

from .models import ImageTag, ImageBed, MyImage


class ImageBedAdmin(admin.ModelAdmin):
    list_display = ('origin_name', 'image_path')


class MyImageAdmin(admin.ModelAdmin):
    list_display = ('origin_name', 'image_path')


admin.site.register(ImageTag)
admin.site.register(ImageBed, ImageBedAdmin)
admin.site.register(MyImage, MyImageAdmin)
