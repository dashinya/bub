from django.http import HttpResponse
from django.shortcuts import render

MENU = {"главная":"/", "пост":"/post", "о блоге":"/about", "Комментарии":"/comment"}

def main_page(request):

        title = "Главная страница"
        data = {"menu":MENU, "title": title}
        return render(request, "./index.html", context=data)

def post_page(request):

        title = "Пост"
        data = {"menu":MENU, "title": title}
        return render(request, "./post.html", context=data)

def about_page(request):

        title = "О блоге"
        data = {"menu":MENU, "title": title}
        return render(request, "./about.html", context=data)