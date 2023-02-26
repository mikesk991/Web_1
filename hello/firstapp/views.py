from django.http import *
from .forms import UserForm
from django.shortcuts import render


def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse(f"<h2>Имя введено корректно - {name}</h2>")
        else:
            return HttpResponse("Ошибка ввода данных")
    else:
        userform = UserForm()
        return render(request, "firstapp/index.html", {"form": userform})
