#coding:utf-8
from django import forms
class LoginForm(forms.Form):
    username=forms.CharField(required=True,error_messages={'invalid':u"用户名不能为空"})
    password=forms.CharField(required=True,min_length=6,error_messages={"invalid":u"密码不能为空且要大于6个字符"})