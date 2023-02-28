from django.http import *
from .models import Person
from django.shortcuts import render


def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})

def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")
