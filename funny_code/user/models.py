from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=11,verbose_name='用户名',unique=True)
    password = models.CharField(max_length=11,verbose_name='密码')
    email = models.CharField(max_length=50,verbose_name='邮箱')
    phone = models.CharField(max_length=11,verbose_name='电话')
    # TODO 写个创建时间和更新时间 

    class Meta:
        db_table = 'user'


class WeiboUser(models.Model):
    uid = models.OneToOneField(UserProfile,null=True)
    access_token = models.CharField(max_length=32,verbose_name='微博token')
    wuid = models.CharField(max_length=11,verbose_name='微博id')

    class Meta:
        db_table = 'weibouser'