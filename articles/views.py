from django.shortcuts import render
from .models import Article

def liste_articles(request):
    articles = Article.objects.all()
    for article in articles:
        if article.promotion:
            article.promo_price = article.prix - (article.prix * article.promotion.pourcentage / 100)
        else:
            article.promo_price = None
    return render(request, 'articles/liste_articles.html', {'articles': articles})


def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'home.html', context)