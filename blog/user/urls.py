
from django.conf.urls import url
from .views import UserRegisterView

urlpatterns = [
    url(r'^$',UserRegisterView.as_view()), # post
    url(r'^/(?P<username>[\w]{1,11})$',UserRegisterView.as_view()) # get
]

