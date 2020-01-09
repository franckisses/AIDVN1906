from django.conf.urls import url
from .views import EmailView,WeiboUrlView,WeiboUserView

urlpatterns = [
    url(r'^/email$', EmailView.as_view()),
    url(r'^/weibo$', WeiboUrlView.as_view()),
    url(r'^/weibo/users$', WeiboUserView.as_view())
]