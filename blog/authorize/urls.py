from django.urls import path
from .views import Authorize, gen_auth_code

urlpatterns = [
    path('', Authorize.as_view(), name='blog'),
    path('auth_code/', gen_auth_code, name='auth_code'),
]
