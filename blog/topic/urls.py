from django.conf.urls import url
from .views import TopicView

urlpatterns = [
    url(r'^/(?P<username>[\w]{1,11})$',TopicView.as_view())
    # url(r'^/(?P<username>[\w]{1,11})$',TopicView.as_view())
]

