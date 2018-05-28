#coding:utf-8
from django.contrib import admin
from iotSystem.models import Data,Warning,SaveWarning
admin.site.site_header=u"IO+物联网后台管理系统"
admin.site.site_title=u"IO+物联网系统"
#Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ("humi","temp","time","pm","jingdu","weidu")
    list_per_page = 30
    ordering = ("-time",)
admin.site.register(Data,DataAdmin)

class WaringAdmin(admin.ModelAdmin):
    list_display=["mailtitle","messageContent","value","level"]

admin.site.register(Warning,WaringAdmin)

class SavewarningAdmin(admin.ModelAdmin):
    list_display = ["warning","currentvalue","time"]

admin.site.register(SaveWarning,SavewarningAdmin)