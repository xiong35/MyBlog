from django.contrib import admin

# Register your models here.
from .models import ArticalTag, Trap, Blog


class TrapAdmin(admin.ModelAdmin):
    list_display = ('problem', 'solution')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('headline',)


admin.site.register(ArticalTag)
admin.site.register(Trap, TrapAdmin)
admin.site.register(Blog, BlogAdmin)
