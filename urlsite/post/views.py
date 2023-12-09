from django.http import HttpResponse
from .models import Comment
from django.shortcuts import render

MENU = {"главная":"/", "пост":"/post", "о блоге":"/about", "Комментарии":"/comment"}


def comment_page(request):
    fullName = request.POST.get('fullName')
    email = request.POST.get('email')
    text = request.POST.get('text')

    print(fullName, email, text)
    if fullName and email and text:
        Comment.objects.create(fullName=fullName, email=email, text=text)

    comments = Comment.objects.filter(checked=True).order_by('-id')
    data = {"menu": MENU, "comments": comments}
    return render(request, './comment.html', context=data)