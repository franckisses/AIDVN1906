from django.db import models
from user.models import UserProfile
# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=50,verbose_name='文章标题')
    category = models.CharField(max_length=10,verbose_name='文章分类')
    limit = models.CharField(max_length=10,verbose_name='文章权限')
    introduce = models.CharField(max_length=90,verbose_name='文件简介')
    content = models.TextField(verbose_name='文章内容')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    # 文章作者
    author = models.ForeignKey(UserProfile)

    class META:
        db_table = 'topic'