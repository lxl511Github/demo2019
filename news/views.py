from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'home.html')

def count(request):
    return render(request,'tong.html')

def nav(request):
    return render(request,'nav.html')

def lis(request):
    list=['https://www.baidu.com','css','js','vue',]
    return render(request,'home.html',{'list':list})
