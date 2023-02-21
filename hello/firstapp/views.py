from django.shortcuts import render

# Create your views here.

def index(request):
    data = {"header": "Передача параметров в шаблон Django",
            "message": "Загружен шаблон templates/firstapp/index_app1.html"}
    return render(request, "firstapp/index_app1.html", context=data)



