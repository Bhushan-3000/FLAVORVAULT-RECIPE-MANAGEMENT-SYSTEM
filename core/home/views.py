from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    peoples = [
        {'name':'abhijeet','age':25},
        {'name':'abhijeet','age':25},
        {'name':'abhijeet','age':25},
        {'name':'abhijeet','age':25},
        {'name':'abhijeet','age':25},
    ]
    return render(request , "index.html", context= {'peoples' : peoples})

def success_page(request):
    return HttpResponse(" <h1>Success Page</h1>")
 