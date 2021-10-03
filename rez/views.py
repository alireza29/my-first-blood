from django.shortcuts import render
from django.http import HttpResponse
def view_rez(request):
    return render(request,'rez\rezo.html',{})