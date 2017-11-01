from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Published'),
    )
    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=10,choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True,
                                help_text="可选项，若为空格则摘取正文钱54个字符")
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        #排序
        ordering = ['-last_modified_time']

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'article_id': self.pk})

class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

class BlogComment(models.Model):
    user_name = models.CharField('评论者名字', max_length=100)
    body = models.TextField('评论内容')
    created_time = models.DateTimeField('评论发表时间', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='评论所属文章')

    def __str__(self):
        return self.body[:20]

class Tag(models.Model):
    name = models.CharField('标签名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

class Suggest(models.Model):
    suggest = models.TextField('意见', max_length=200)
    suggest_time = models.DateTimeField('提出时间', auto_now_add=True)

    def __str__(self):
        return self.suggest
