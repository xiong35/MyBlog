from django.contrib import admin

from .models import Question, Visiter


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'category')


class VisiterAdmin(admin.ModelAdmin):
    list_display = ('expire', 'authority')


admin.site.register(Visiter, VisiterAdmin)
admin.site.register(Question, QuestionAdmin)
