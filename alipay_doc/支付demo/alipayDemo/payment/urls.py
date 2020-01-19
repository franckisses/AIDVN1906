from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^jump/', views.OrderProcessingnView.as_view()),
    url(r'^result/', views.PaymentResultView.as_view())
]