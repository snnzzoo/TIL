from django.shortcuts import render, redirect
from articles.forms import ArticleForm
from .models import Article


# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index') # 나중에 상세글 페이지로 변경!
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/create.html', context)


