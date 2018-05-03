from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from myapp.models import User


def test_cookie(request):
    #获取cookie信息
    # request.COOKIES


    #响应
    resp = render(request,"test02_index.html")
    resp = HttpResponse('')
    reqsp = redirect()
    resp.set_cookie()

    resp.set_cookie("username","zhangsan")

def test_cookie2(request):
    resp = render(request,"test02_index.html")
    username = request.get_signed_cookie("username",default="",salt="test")
    if not username:
        resp
        pass
    return resp

#关于setting技术
"""
 在settings.py中要开启，如果用会话柱子中技术关闭
 djangp处理session数据的方式
 1 存在数据库中
 2 缓存中
 3 文件中
 4 缓存 + 数据库中
 5 加密cookie
 6 Django - redius - session （第三方中，需要单独进行安装）
"""
def test_session(request):
    # request.session["username"]
    username = request.session.get("username",default=None)
    #设置值 ,如果存在就修改，不存在进进行设置
    request.session.setdefault("username","1231321")
    request.session["user"] = "123132"
    #获取所有的key值


def test_session2(request):
    request.session.setdefault("username","123")
    return render(request,"test02_index.html")

#session 实现免登录
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = User.objects.filter(username=username,password=password).first()
    if user:
        request.session.setdefault("username",user.name)











