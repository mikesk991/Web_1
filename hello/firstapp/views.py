from django.http import *
from .forms import UserForm
from django.shortcuts import render


def index(request):
    if request.method == "POST":
        name = request.POST.get ("name") # получить значение поля Имя
        age = request.POST.get("age")  # получить значение поля Возраст
        output = f"<h2>Пользователь</h2><h3>Имя - {name},Возраст - {age}</hЗ>"
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "firstapp/index.html", {"form": userform})
