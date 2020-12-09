# -*- coding: utf-8 -*-

from django.urls import path
from .views import HomePageView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView  # firstly import class then add it to patterns

urlpatterns = [
    
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('article/new/', ArticleCreateView.as_view(), name='new_article'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('', HomePageView.as_view(), name='home'),
    ]