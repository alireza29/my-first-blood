from django.shortcuts import render
from django.http import HttpResponse
def view_gallery(request):
    return HttpResponse("Wellcome to the Gallery Section")

