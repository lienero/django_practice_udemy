from django.urls import path
from . import views


urlpatterns = [
    path('author', views.author),
    path('book', views.book)
]
