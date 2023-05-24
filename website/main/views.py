from django.shortcuts import render

def index(request):
    data = {
        "title": "Главная страница",
        "values": ["some", "hello", "1234"],
        "obj": {
            "car": "BMW",
            "age": "2020",
            "hobby": "basketball",
        }
    }
    return render(request, "main/index.html", data )

def about(request):
    return render(request, "main/about.html")
