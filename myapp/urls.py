from django.conf.urls import url
from myapp import views
urlpatterns = [
    url('register/',views.register),
    url('update/',views.update),
    url('login',views.login),
]


# from django.conf.urls import url
#
# from test01 import views
#
# urlpatterns = [
#     url('register/', views.register),
# ]