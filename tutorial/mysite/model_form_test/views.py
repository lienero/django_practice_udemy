from django.shortcuts import render
from .forms import AuthorForm, BookForm


def author(request):
    form = AuthorForm()
    return render(request, 'form_test/author.html', {'form': form})


def book(request):
    form = BookForm()
    return render(request, 'form_test/book.html', {'form': form})

# Create your views here.
