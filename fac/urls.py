from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_f,name='view_f'),
    path('<int:n>',views.view_fac,name='view_fac')
]