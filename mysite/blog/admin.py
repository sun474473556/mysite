from django.contrib import admin
from .models import Article, Category, BlogComment, Tag
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time')
admin.site.register([Category, BlogComment, Tag])
admin.site.register(Article, ArticleAdmin)
# Register your models here.
