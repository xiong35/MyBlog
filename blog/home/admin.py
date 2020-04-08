from django.contrib import admin
from .models import Statistic


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('item', 'count')


admin.site.register(Statistic, StatisticAdmin)
