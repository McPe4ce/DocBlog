from django.urls import path
from blog.views import index, article

urlpatterns = [
    path('', index, name="blog-index"),
    path('article-<str:num_article>/', article, name="blog-article"),
]