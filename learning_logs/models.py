#coding = utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Topic(models.Model):

    text = models.CharField(max_length=200)
    #CharField 定义文本信息,max_lenght 必须属性,输入的最大字节数目

    time_added = models.DateField(auto_now_add=True)
    #DateField 表示日期 auto_now_add=True 自动添加日期
    owner = models.ForeignKey(User,on_delete=True)
    #user类是系统内置的类
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=True)  #外键关联到Topic  级联
    text = models.TextField() #文本区域,不需要输入长度
    data_added = models.DateTimeField(auto_now_add=True) #自动添加时间.相当于一个时间戳
    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.text[:50] + "..."  #默认显示文本的前50个字符



