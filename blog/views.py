from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    blog_count = Blog.objects.count
    blog_articles = Blog.objects.order_by('-published_date')
    return render(request, 'blog/all_blogs.html', {'articles': blog_articles, 'blog_count': blog_count})

def detail(request, blog_id):
    blog_article = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog_article': blog_article})