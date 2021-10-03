from django.shortcuts import render
from django.http import HttpResponse
def view_by(request):
    return HttpResponse("Goodbye")