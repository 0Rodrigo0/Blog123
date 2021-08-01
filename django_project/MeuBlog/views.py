from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPosView(CreateView):
    model = Post
    template_name = 'faca_seu_post.html'
    #fields = '__all__'
    fields = ('title', 'body', 'title_tag')

