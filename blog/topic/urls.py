from django.conf.urls import url
from .views import TopicView

urlpatterns = [
    url(r'^/(?P<username>[\w]{1,11})$',TopicView.as_view())
    # url(r'^/(?P<username>[\w]{1,11})$',TopicView.as_view())
]
"""
# 博客查询：

    用户登录  
        获取全量数据 公开的私有的
        获取部分数据 ？tec no-tec

    用户未登录
        获取全量的公开的数据
        获取部分数据 tec no-tec

"""
