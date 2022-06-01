from multiprocessing import context
from django.shortcuts import render

from .models import Article


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'articel_list': a_list}
    return render(request, 'news/year_archibe.html', context)
