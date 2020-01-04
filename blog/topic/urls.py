from django.conf.urls import url
from .views import TopicView

urlpatterns = [
    url(r'^/(?P<username>[\w]{1,11})$',TopicView.as_view())
    # url(r'^/(?P<username>[\w]{1,11})$',TopicView.as_view())
]

# http://127.0.0.1:8000/v1/topics/franck