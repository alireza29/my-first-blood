from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_hello,name='view_hello'),
    path('details/',views.view_details,name='view_details')
]

