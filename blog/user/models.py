from django.db import models

# Create your models here.
class UserProfile(models.Model):
    # 用户名
    username = models.CharField(max_length=11, 
        verbose_name='用户名', primary_key=True)
    nickname = models.CharField(max_length=30, 
    verbose_name='昵称')
    email = models.CharField(max_length=50,
    verbose_name='邮箱')
    password = models.CharField(max_length=32)
    sign = models.CharField(max_length=50,
        verbose_name='用户签名')
    info = models.CharField(max_length=150,
        verbose_name='用户个人介绍')
    avatar = models.ImageField(upload_to='avatar/')

    class Meta:
        db_table = 'user'
    