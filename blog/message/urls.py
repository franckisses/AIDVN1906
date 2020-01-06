from django.conf.urls import url
from .views import MessageView

urlpatterns = [
    url(r'^/(?P<topic_id>[\d]+)$',MessageView.as_view())
]


# python3 manage.py startapp message
# installed_apps + 'message'
# 配置主路由中的应用分路由　
# 在message 中添加了一个urls.py