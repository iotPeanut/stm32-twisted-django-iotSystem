#coding:utf-8
from django.shortcuts import render
from users.models import UserProfile
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from forms import LoginForm
from django.views.generic.base import View
from django.core.urlresolvers import reverse
# Create your views here.
class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("iotSystem:index"))  # 直接跳转到另一个app的页面中
        return render(request,"login.html",{})
    def post(self,request):
        login_form=LoginForm(request.POST)  #验证表单
        if request.user.is_authenticated():
            return   HttpResponseRedirect(reverse("iotSystem:index"))   #直接跳转到另一个app的页面中
        if login_form.is_valid():
            username=request.POST.get("username","")
            password=request.POST.get("password","")
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)  #登入
                #return HttpResponseRedirect()    #登入到用户的页面
                return HttpResponseRedirect(reverse("iotSystem:index"))
            else:
                return render(request,"login.html",{"msg":u"用户名或密码错误！"})
        else:
            return render(request,"login.html",{"login_form":login_form})
class LogoutView(View):
    def get(self,request):
        logout(request)    #登出
        return HttpResponseRedirect(reverse("users:login"))  #跳转到登陆

