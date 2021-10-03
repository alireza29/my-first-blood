from django.shortcuts import render
from django.http import HttpResponse


def view_cadd(request):
    return HttpResponse('jangle')
def view_ctel(request):
    return HttpResponse('021-210-210-21')
def view_cmob(request):
    return HttpResponse("0912-222-22-91")