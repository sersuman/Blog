from django.urls import path
from .views import ArticleView, SingleArticleView

app_name = 'articles'
# app_name will help us to do reverse look up latter

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>/', ArticleView.as_view()),
    path('articles/<int:pk>', SingleArticleView.as_view()),
]
