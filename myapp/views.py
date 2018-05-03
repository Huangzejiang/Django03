from pydoc import text

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import User

#注册
def register(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    result = "注册失败"
    try:
        #通过用户名，返回一个QuerySet对象
        user = User.objects.filter(username=username)
        if user:
            result = "用户已经存在"
        else:
            User.objects.create(username=username,password=password)
            result = "注册成功"
    except:
        pass
    return HttpResponse(result)

#登录
def login(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    try:
        user = User.objects.get(username=username)
        if user:
            if user.password == password:
                return HttpResponse("登录成功")
            else:
                return HttpResponse("密码错误")
        else:
            return HttpResponse("账号不存在")
    except:
        return HttpResponse("网络异常")

#更新
def update(request):
    uid = request.GET.get("uid")
    username = request.GET.get("username")
    password = request.GET.get("password")
    result = "更新失败"
    try:
        # User.objects.filter(uid=uid).update(username=username,password=password)
        temp = User.objects.filter(uid=uid)
        print(temp,type(temp))
        temp.update(username=username,password=password)
        result = "更新成功"
    except:
        pass
    return HttpResponse(result)


def register(request):
    return None