from django.urls import path
from app2.views import *
app1_name='ravi'

urlpatterns=[
    path('ravi/',ravi,name='ravi'),
    path('teja/',teja,name='teja'),
]