from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post




# def home(request):
#     return render(request,'home.html',{ })



class HomeView(ListView):
    model = Post
    template_name= 'home.html'

class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'

# def home(request):
#
#     test_list=Post.objects.all()
#
#     return render(request,'home.html',{'test_list':test_list})
#
# def article(request,article_id):
#
#     test_list=Post.objects.get(pk=article_id)
#
#     return render(request,'templates/article.html',{'test_list':test_list})