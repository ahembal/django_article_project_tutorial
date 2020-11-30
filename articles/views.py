from django.views.generic import ListView, DetailView
from .models import Article

class HomePageView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'all_articles_list'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'