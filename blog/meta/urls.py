from django.urls import path
from .views import BlogMeta, Duck

urlpatterns = [
    path('', BlogMeta.as_view(), name='meta'),
    path('duck/', Duck.as_view(), name='duck'),
]
