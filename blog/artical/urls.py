from django.urls import path
from .views import Blog, Tag, Trap

urlpatterns = [
    path('blog/', Blog.as_view(), name='blog'),
    path('trap/', Trap.as_view(), name='trap'),
    path('tag/', Tag.as_view(), name='tag'),
]
