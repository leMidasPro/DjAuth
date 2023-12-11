from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponse
from django.template.loader import render_to_string


def art_lst(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/art_ls.html', {'articles': articles})


def art_det(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/art_det.html', {'article': article})


@login_required(login_url="/accounts/login/")
def art_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('article:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/art_create.html', {'form': form})
