
from django.conf.urls import url
from .views import UserRegisterView,UserAvatarView

urlpatterns = [
    url(r'^$',UserRegisterView.as_view()), # post
    url(r'^/(?P<username>[\w]{1,11})$',UserRegisterView.as_view()), # get
    url(r'^/(?P<username>[\w]{1,11})/avatar$',UserAvatarView.as_view())
]
