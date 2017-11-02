from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete

app_name = 'blog'
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
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),
    url(r'^password-reset/$', password_reset, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete, name='password_reset_complete'),
]
