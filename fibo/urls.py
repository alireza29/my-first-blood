from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_fibo,name='view_fibo'),
]