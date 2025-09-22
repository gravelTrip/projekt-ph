from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")
def administratorzy(request):
    return render(request, "administratorzy/lista_administratorow.html")