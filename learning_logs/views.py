from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.db import models
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
# Create your views here.
def index(request):
	"""学习笔记的主页"""

	#调用模板并响应，未接收参数
	return render(request,'learning_logs/index.html')

@login_required		#限制未登录的访问
def topics(request):
	"""显示所有的主题"""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	#上下文：是个字典，一般封装从数据库中查询出来的数据
	context = {'topics':topics}

	# 渲染模板并响应，接受一个上下文作为参数，传递给模板
	return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
	"""显示单个主题及其所有条目"""
	topic = Topic.objects.get(id=topic_id)
	#确认请求的主题属于当前用户
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic,'entries':entries}
	return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
	"""添加新主题"""
	if request.method != 'POST':
		# 未提交表单：创建一个新表单
		form = TopicForm()
	else:
		# POST提交的数据，对数据进行处理
		form = TopicForm(request.POST)
		if	form.is_valid():
			# form.save()		#当前没有将新主题关联到特定用户，
 			# 当添加新主题时将报Exception Type:	IntegrityError
			# Exception Value:	NOT NULL constraint failed: learning_logs_topic.owner_id
			# 解决方案：
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form':form}
	return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
	"""在特定的主题中添加新条目"""
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		# 未提交数据：创建一个新表单
		form = EntryForm()
	else:
		# POST提交的数据，对数据进行处理
		form = EntryForm(data=request.POST)
		if	form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))

	context = {'topic':topic,'form':form}
	return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
	"""编辑既有条目"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:		# 保护编辑页面
		raise Http404
	if request.method != 'POST':
		# 初次请求，使用当前条目填充表单
		form = EntryForm(instance=entry)	#s使用既有条目对象中的信息填充它

	else:
		# POST提交的数据，对数据进行处理
		form = EntryForm(instance=entry,data=request.POST)
		if	form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))

	context = {'entry':entry,'topic':topic,'form':form}
	return render(request,'learning_logs/edit_entry.html',context)


