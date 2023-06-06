
from django.shortcuts import render


def pageNotFound(request, exception):
    return render(request, 'main/404.html')

def index(request):
    data = {"title": "Главная страница",
            "values": ["Наука и инновации", "Медиа", "Университет", "Поступающим", "Обучающимся"]
            }

    return render(request, "main/index.html",data)

def about(request):
    return render(request, "main/about.html")


def contacts(request):
    data = {
        "title": "Контакты",
        "values": ["+7 (499) 263-65-41", "bauman@bmstu.ru", "105005, Москва, 2-я Бауманская ул., д. 5, корп. 1", "ПН-СБ 08:00–22:00"]
            }

    return render(request, "main/contacts.html", data)
