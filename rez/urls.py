from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_rez,name='view_rez')
]