#coding:utf-8
import time
from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from iotSystem.models import Data,Warning,SaveWarning
import datetime
import json
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from WEB.settings import EMAIL_FROM
from django.core.mail import send_mail
def data_dis(request):
    if request.user.is_authenticated():
        datas = Data.objects.order_by("-time").values("time","humi","temp","pm")[:30]
        datas=list(datas)
        for data in datas:
             data["time"]=data["time"].strftime("%Y/%m/%d %H:%M:%S")
        datas=json.dumps(datas[::1])
        return render(request, "index_v1.html", {"data_list": datas})
    else:
        return render(request,"index_v1.html",{"msg":u"无权查看"})

def index(request):
    if request.user.is_authenticated():
        return render(request,"index.html",{"msg":u"成功进入"})
    else:
        return render(request,"login.html",{"msg":u"无权查看"})
def data_in(request):
    if request.method == "GET":
        temp=request.GET.get("temp", "50")
        humi=request.GET.get("humi", "120")
        pm= request.GET.get("pm", "320")
        data=Data(temp=temp,humi=humi,pm=pm)
        data.save()
        return HttpResponse("OK")


#ajax请求新的气体数据
time1=""
average=[]
value=0
timesend=0
def ajax_data(request):
    global time1, average, value, timesend
    data = Data.objects.order_by("-time").values("time", "humi", "temp", "pm")[0]
    if time1 != data["time"]:
        time1 = data["time"]
        if len(average) == 5:
            warning = Warning.objects.get(level="primary")
            msgContent = warning.messageContent
            mailtitle = warning.mailtitle
            interval = warning.interval
            valueWarning = warning.value
            value = reduce(lambda x, y: x + y, map(int, average)) / len(average)
            if int(time.time()) >= timesend + int(interval) * 60:
                if value >= int(valueWarning):
                    # send message and save warnring msg
                    timesend = int(time.time())
                    send_mail(mailtitle, msgContent, EMAIL_FROM, ["1531400516@qq.com"])
                    SaveWarning.objects.create(warning=warning, currentvalue=value)
                average = []
        else:
            average.append(data["temp"])
    data["time"] = data["time"].strftime("%Y/%m/%d %H:%M:%S")
   # resp={"ch1":q1.value,"time1":q1.time.strftime("%Y/%m/%d %H:%M:%S"),"ch2":q2.value,"time2":q2.time.strftime("%Y/%m/%d %H:%M:%S")}
   # resp = {"temp": data.temp,"humi":data.humi,"ch4":data.ch4, "time": data.time.strftime("%Y/%m/%d %H:%M:%S")}
    return HttpResponse(json.dumps(data),content_type="application/json")

#查询历史数据
def data_history(request):
    datas=Data.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(datas, 8, request=request)
    data=p.page(page)
    return render(request,"index_v2.html",{"data":data})


def position(request):
    return render(request,"position.html")
def historyDataFilter(request):
    if request.method=="GET":
        #返回最近的100条数据
        datas = Data.objects.order_by("-time").values("time", "humi", "temp", "pm")[:100]
        datas = list(datas)
        for data in datas:
            data["time"] = data["time"].strftime("%Y/%m/%d %H:%M:%S")
        datas = json.dumps(datas[::1])
        return render(request, "historyDataFilter.html", {"data_list": datas})
    else:
        start=request.POST.get("start","no")
        end=request.POST.get("end","no")
        time=request.POST.get("time","no")
        start=datetime.datetime.strptime(start,"%Y/%m/%d %H:%M:%S")
        end= datetime.datetime.strptime(end,"%Y/%m/%d %H:%M:%S")
        datas=Data.objects.values("time","humi","temp","pm").filter(time__range=(start,end))
        for data in datas:
            data["time"] = data["time"].strftime("%Y/%m/%d %H:%M:%S")
        datas = json.dumps(datas[::1])
        return render(request,"historyDataFilter.html",{"data_list": datas})

    #return render(request,"historyDataFilter.html")
def control(request):
    return render(request,"control.html")

def introduce(request):
    return render(request,"introduce.html")
def background(request):
    return render(request,"background.html")

def warningHistory(request):
    datas=SaveWarning.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(datas, 8, request=request)
    data = p.page(page)
    return render(request, "warning.html", {"data": data})