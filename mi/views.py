from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bumrah(request):
    return render(request,'bumrah.html')

def rohit(request):
    return HttpResponse('<h1>hi this is rohit sharma</h1>')