from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'news/list_news.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})

def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('article_list')
    return render(request, 'news/create_news.html')

def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('article_detail', pk=article.pk)
    return render(request, 'news/update_news.html', {'article': article})

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'news/delete_news.html', {'article': article})
