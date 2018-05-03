from django.conf.urls import url

from test01 import views

urlpatterns = [
    url('register/', views.register),
]