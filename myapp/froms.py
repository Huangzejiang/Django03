#专门用来存放form对象
"""
1 第一步:先定义对象
2
"""
from django.forms import forms


class TestForm(forms.Form):
    username = forms.CharField()