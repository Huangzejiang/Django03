from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from test01.forms import TestForm, UserModelForm



def register(request):
    print(request,type(request))
    if request.method == 'POST':
        user_form = UserModelForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse('验证成功')
    else:
        user_form = UserModelForm()
    return render(request, 'form01.html', {'user_form': user_form})