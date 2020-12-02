# -*- coding: utf-8 -*-

from django.urls import path
from .views import HomePageView, ArticleDetailView, ArticleCreateView

urlpatterns = [
    path('article/new/', ArticleCreateView.as_view(), name='new_article'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('', HomePageView.as_view(), name='home'),
    ]