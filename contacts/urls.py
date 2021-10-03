from django.urls import path
from . import views

urlpatterns = [
    path('add',views.view_cadd,name='view_cadd'),
    path('tel',views.view_ctel,name='view_ctel'),
    path('mob',views.view_cmob,name='view_cmob'),
]