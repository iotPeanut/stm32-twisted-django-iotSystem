#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name=u'昵称',default='')
    class Meta:
        verbose_name=u'用户信息'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.username