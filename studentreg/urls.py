from django.urls import path
# from .import views
from .views import HomeView, ArticleView


urlpatterns = [
    # path('', views.home, name="home"),
    # path('article/<article_id>', views.article, name="article-y"),
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleView.as_view(), name='article-detail'),

]