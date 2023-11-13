from rcb.views import *
from django.urls import path
app_name = 'banglore'
urlpatterns = [
    path('virat/', virat, name='virat'),
    path('abd/', abd, name='abd'),



]