from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from learning_logs.forms import TopicForm, EntryForm
from learning_logs.models import Topic, Entry


def index_view(request):
    return render(request,"index.html")

@login_required  #加login_required装饰器,可显示用户访问
def topics_view(request):
    topics = Topic.objects.filter(owner=request.user).order_by("time_added") #从数据库总,通过模型类获取到所有一个queryset
    return render(request, "topics.html", {"topics":topics})

@login_required
def topic_view(request,topic_id):
    topic = Topic.objects.get(id = topic_id)  #根据前台传入的html传入的topic_id获取对应的topic
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by("data_added") #根据外键查询对应topic下的ertries
    return render(request,"topic.html",{"topic":topic,"entries":entries})

@login_required
def new_topic_view(request):
    if request.method != "POST":  # 刚进入网页时 get请求,此时是一个空的表单
        form = TopicForm()  #生成一个空的表单
    else:
        form = TopicForm(request.POST)  #提交数据之后,根据post请求,创建表单.重定向回到topic页面
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse("topics"))
    return render(request,"new_topic.html",{"form":form})

@login_required
def new_entry_view(request,topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse("topic",args=[topic_id]))

    return render(request,"new_entry.html",{"topic":topic,"form":form})

@login_required
def edit_entry_view(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.owner:
        raise Http404

    if request.method != "POST":
        form = EntryForm(instance=entry)
        # 第一次访问是属于get请求,需要创建一个空表单,参数 instance = entry 使用当前获取到的条目填充表单
    else:
        form = EntryForm(instance=entry,data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("topic",args=[topic.id]))
    return render(request,"edit_entry.html",{"entry":entry,"topic":topic,"form":form})