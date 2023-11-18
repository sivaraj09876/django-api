from django.urls import path
from .views import *

urlpatterns=[
    path('',get_api,name='get_api')
]