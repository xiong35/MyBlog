from django.urls import path
from .views import Highlighter

urlpatterns = [
    path('highlighter/', Highlighter.as_view(), name='highlighter'),
]
