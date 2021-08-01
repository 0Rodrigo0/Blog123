from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPosView, UpdatePostView

urlpatterns = [
    #path('', views.home, name="home"),
    path('',  HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('faca_seu_post/', AddPosView.as_view(), name='Faca_Seu_Post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
]
