from django.shortcuts import render
from django.http import HttpResponse

def view_fibo(request):
    i=1
    j=0
    l=''
    for k in range(1000):
        l+=f'{i}'+'<br>'
        i, j=i+j, i
    return HttpResponse(l)