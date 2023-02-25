from django.shortcuts import render

# Create your views here.

def index(request):
    cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
    return render(request, "firstapp/index.html", context={"cat": cat})



