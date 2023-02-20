from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def products(request, productid=1):
    output = f"<h2> Продукт № {productid}</h2>"
    return HttpResponse(output)

def users(request, id, name):
    output = f"<h2>Пользователь</h2><h3>id: {id} Имя:{name}"
    return HttpResponse(output)
