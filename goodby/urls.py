from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_by,name='view_by')
]
