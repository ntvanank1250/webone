from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'main/home.html')
   

def first(request):
    return render(request,'main/first.html')
def second(request):
    return render(request,'main/second.html')
def third(request):
    return render(request,'main/third.html')
