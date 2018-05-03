#表示导入models模块
from django.db import models

# Create your models here.
class User(models.Model):
    #数据库中创建主键,primary_key表示主键的自动增长
    uid = models.AutoField(primary_key=True)
    #char对应varchar数据类型
    username = models.CharField(max_length=32)
    #密码
    password = models.CharField(max_length=32)
    #性别
    sex = models.IntegerField()
    #手机
    # phone = models.CharField(max_length=7,decimal_places=2)
    #decimal(7,2).数字总长度，7小数点2
    # models.DecimalField(max_digits=7,decimal_places=2)
    #年月日
    create_date = models.DateField(auto_now_add=True)
    #年月日时分秒
    last_time = models.DateTimeField(auto_now=True)
