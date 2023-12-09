from django.urls import path, include

from .views import comment_page

urlpatterns = [
    path('', comment_page, name="comment" ),
]
