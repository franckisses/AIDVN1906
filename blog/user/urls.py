
from django.conf.urls import url
from .views import UserRegisterView

urlpatterns = [
    url(r'^$',UserRegisterView.as_view())
]