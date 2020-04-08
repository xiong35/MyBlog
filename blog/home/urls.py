from django.urls import path
from .views import get_all_tags

urlpatterns = [
    path('get_all_tags/', get_all_tags, name='get_all_tags'),
]
