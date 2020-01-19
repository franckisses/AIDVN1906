from  django.conf.urls import url
from .views import EmailView,WeiboUrlView,WeiboUserView,RedisView,ActiveView

urlpatterns = [
    url(r'^/email$', EmailView.as_view()),
    url(r'^/weibo$', WeiboUrlView.as_view()),
    url(r'^/weibo/users$', WeiboUserView.as_view()),
    url(r'^/test$', RedisView.as_view()),
    url(r'^/active$',ActiveView.as_view())
]