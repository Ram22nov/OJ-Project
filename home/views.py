from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def practice(request):
    return HttpResponse("this is practice page")

def contest(request):
    return HttpResponse("this is contest page")

def profile(request):
    return HttpResponse("this is practice page")

def discuss(request):
    return HttpResponse("this is discussion page")
