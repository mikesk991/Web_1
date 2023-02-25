from django.shortcuts import render
from .forms import UserForm

# Create your views here.


def index(request):
    userform = UserForm()
    return render(request, "firstapp/index.html", context={"form": userform})
