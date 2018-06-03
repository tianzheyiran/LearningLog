from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def logout_view(request):
    '''注销用户的视图函数'''
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register_view(request):
    '''注册新用户'''
    if request.method != "POST":
        #显示一个空的表单
        form=UserCreationForm()
    else:
        #post请求会提交数据过来,狐狸提交的数据
        form = UserCreationForm(data=request.POST)
        #数据校验
        if form.is_valid():
            new_user = form.save()  #保存用户注册的信息
            authenticated_user = authenticate(username = new_user.username,password=request.POST["password1"])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse("index"))
    return render(request,"register.html",{"form":form})

