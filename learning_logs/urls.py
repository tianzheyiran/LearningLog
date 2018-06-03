#coding=utf-8
# learning_logs的urls配置
from django.conf.urls import url

from learning_logs import views

urlpatterns=[
    url(r"^$", views.index_view, name="index"),
    # url可以接收三个参数,第三个参数相当于为url模版命名,
    # 在项目中其他地方使用这个主页链接时时,只需要调用name的值就可以了
    # 一般主要用在html中做网页链接用
    url(r"^topics/$",views.topics_view,name="topics"),
    url(r"^topics/(?P<topic_id>\d+)/",views.topic_view,name="topic"),
    url(r"^new_topic/",views.new_topic_view,name = "new_topic"),
    url(r"^new_entry/(?P<topic_id>\d+)/$",views.new_entry_view,name="new_entry"),
    url(r"^edit_entry/(?P<entry_id>\d+)/$",views.edit_entry_view,name="edit_entry"),
    #注意正则的使用
]