from django.template.response import TemplateResponse

# Create your views here.

def index(request):
    header = "Персональные данные"
    langs = ["Английский","Немецкий","Испанский"]
    user = {"name": "Максим", "age": 30}
    addr = ("Виноградная", 23, 45)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return TemplateResponse(request, "index.html", data)



