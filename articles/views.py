from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import Article

class HomePageView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'all_articles_list'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    
class ArticleCreateView(CreateView):
    model = Article
    template_name = 'new_article.html'
    fields = ['title', 'author', 'text', 'photo' ] # Sometimes for security reasons os can block adding photos
    
class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'text' ]  