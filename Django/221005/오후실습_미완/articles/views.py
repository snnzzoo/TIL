from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

# 요청 정보를 받아서


def index(request):
    # 게시글을 가져와서
    articles = Article.objects.order_by('-pk')
    # template에 전달한다.
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form': article_form
#     }
#     return render(request, 'articles/new.html', context=context)


def create(request):
    if request.method == 'POST':
        # DB에 저장
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        # 유효하지 않을 경우
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Article.objects.create(title=title, content=content)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
