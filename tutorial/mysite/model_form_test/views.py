from django.shortcuts import render
from .forms import AuthorForm, BookForm


def author(request):
    form = AuthorForm()
    return render(request, 'form_test/author.html', {'from': form})


def book(request):
    form = BookForm()
    return render(request, 'from_test/book.html', {'from': form})

# Create your views here.
