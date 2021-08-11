from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def main_home(request):
    result={}
    return render(request, 'main_home.html', context=result)

def page01(request):
    result={}
    return render(request, 'page01.html', context=result)
