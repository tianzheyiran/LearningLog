#coding=utf-8
from django.conf.urls import url
from django.contrib.auth.views import login

from users import views

urlpatterns = [
    url(r"^login/$",login,{"template_name":"login.html"},name="login"),

    #url第一个参数是正则,第二个参数时view,该例中导入了django默认的登录视图 login
    # 传递一个字典,告知url去 ueser下取找 login.html页面,
    #该url命名为 login
    url(r"^logout/$",views.logout_view,name="logout"),
    url(r"^register/$",views.register_view,name="register"),
]