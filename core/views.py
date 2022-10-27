from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def pro(request):
    return render(request, 'core/ex_pro.html')

def Log(request):
    return render(request, 'core/registration/login.html')