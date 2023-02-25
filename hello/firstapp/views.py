from django.shortcuts import render

# Create your views here.

def index(request):
    data = {"age": 67}
    return render(request, "firstapp/index.html", context=data)



