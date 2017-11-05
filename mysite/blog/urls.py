from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout_then_login


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^addarticle', views.addArticle, name='add'),
    url(r'^article/(?P<article_id>\d+)$', cache_page(60 * 15)(views.ArticleDetailView.as_view()), name='detail'),
    url(r"^category/(?P<cate_id>\d+)$", views.CategoryView.as_view(), name='category'),
    url(r'^article/(?P<article_id>\d+)/comment/$', views.CommentView, name='comment'),
    url(r'^search/$', views.blog_search, name='search'),
    url(r'^about_me/$', views.suggest_view, name='about_me'),
    url(r'^tags/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
]
