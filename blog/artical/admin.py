from django.contrib import admin

# Register your models here.
from .models import ArticalTag, Trap, Blog


class TrapAdmin(admin.ModelAdmin):
    list_display = ('problem', 'solution')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('headline',)


class ArticalTagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'count')


admin.site.register(ArticalTag, ArticalTagAdmin)
admin.site.register(Trap, TrapAdmin)
admin.site.register(Blog, BlogAdmin)
