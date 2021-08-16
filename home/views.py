from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def main_home(request):
    result={}
    return render(request, 'main_home.html', context=result)

def tech(request):
    result={}
    return render(request, 'tech.html', context=result)

def fashion(request):
    result={}
    return render(request, 'fashion.html', context=result)

def beauty(request):
    result={}
    return render(request, 'beauty.html', context=result)

def food(request):
    result={}
    return render(request, 'food.html', context=result)

def living(request):
    result={}
    return render(request, 'living.html', context=result)
