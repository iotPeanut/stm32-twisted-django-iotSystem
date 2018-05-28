#coding:utf-8
from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^data_dis/$', views.data_dis, name='data_dis'),
    #url(r'^state_in/$',views.state_in,name="state_in"),
    url(r'^data_history/$',views.data_history,name="data_history"),
    url(r"data_in/$",views.data_in,name="data_in"),
    url(r"ajax_data/$", views.ajax_data, name="ajax_data"),
   #url(r"^dataShow/$",views.dataShow,name="dataShow"),
    url(r"^position/$", views.position, name="position"),
    url(r"^historyDataFilter/$", views.historyDataFilter, name="historyDataFilter"),
    url(r"^introduce/$", views.introduce, name="introduce"),
    url(r"^background/$", views.background, name="background"),
    url(r"^warningHistory/$", views.warningHistory, name="warningHistory"),
    url(r"^control/$", views.control, name="control"),
]