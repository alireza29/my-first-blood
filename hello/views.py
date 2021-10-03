from django.shortcuts import render
from django.http import HttpResponse
def view_hello(request):
    return HttpResponse("Hello")
def view_details(request):
    return render(request,'hello\details.html',{})