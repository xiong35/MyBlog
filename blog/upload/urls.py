from django.urls import path
from .views import thumbup, question, image, comment

urlpatterns = [
    path('thumbup/', thumbup, name='thumbup'),
    path('question/', question, name='question'),
    path('comment/', comment, name='comment'),
    path('image/', image, name='image'),
]
