from django.urls import path
from .views import BlogMeta

urlpatterns = [
    path('', BlogMeta.as_view(), name='meta'),
]
