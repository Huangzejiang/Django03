from django.conf.urls import url

from test02 import views

urlpatterns = [
    url('test_session/', views.test_session),
]