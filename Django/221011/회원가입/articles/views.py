from django.shortcuts import render, redirect
from articles.models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 게시글을 가져와서
    articles = Article.objects.order_by('-pk')
    # template에 뿌려준다.
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        # DB에 저장
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context=context)


def detail(request, pk):
    # 특정 글을 가져와서
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article': article,
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)


def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')
