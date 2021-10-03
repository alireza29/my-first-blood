from django.shortcuts import render
from django.http import HttpResponse
def fac(n):
    for i in range(1,n):
        n*=i
    return n
def view_f(request):
    l=''
    for i in range(1,1001):
        l+=f'{i}!: {fac(i)}'+'<br>'
    return HttpResponse(l)
def view_fac(request,n):
    return HttpResponse(fac(n))
