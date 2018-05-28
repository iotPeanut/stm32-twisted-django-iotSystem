#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.
class Data(models.Model):
    humi=models.CharField(max_length=20,default="",verbose_name=u"湿度")
    temp=models.CharField(max_length=20,default="",verbose_name=u"温度")
    #at=models.CharField(max_length=20,default="",verbose_name=u"光照")
    pm= models.CharField(max_length=20, default='',verbose_name=u"粉尘")
    #position args
    jingdu = models.CharField(max_length=20, default='', verbose_name=u"经度")
    weidu = models.CharField(max_length=20, default='', verbose_name=u"维度")

    time=models.DateTimeField(default=datetime.now,verbose_name=u"采集数据时间")
    class Meta:
        ordering=("time",)
        verbose_name=u"数据信息"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Warning(models.Model):
    mailtitle=models.CharField(max_length=50,default="浓度超标了",verbose_name=u"邮件标题")
    messageContent=models.TextField(default="报警！",verbose_name=u"报警内容")
    value=models.IntegerField(default=100,verbose_name=u"阈值")
    interval=models.IntegerField(default=10,verbose_name=u"报警时间间隔")
    level=models.CharField(max_length=20,default="primary",choices=(("primary","初级报警"),("serious","严重报警"),("fatal","致命报警")),verbose_name="报警类型");
    class Meta:
        verbose_name=u"报警信息"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.level
class SaveWarning(models.Model):
    warning=models.ForeignKey(Warning,verbose_name="所属报警")
    currentvalue=models.CharField(max_length=10,default="",verbose_name=u"报警平均值")
    time = models.DateTimeField(default=datetime.now, verbose_name=u"报警时间")
    class Meta:
        verbose_name=u"报警信息记录"
        verbose_name_plural=verbose_name