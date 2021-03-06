"""
learning_logs URL Configuration
"""
from django.urls import path,re_path
from . import views

urlpatterns = [
	#主页
    path('',views.index,name='index'),
    
    #显示所有的主题
    path('topics/',views.topics,name='topics'),
    
    #显示特定主题的详细页面
    re_path(r'topics/(?P<topic_id>\d+)/',views.topic,name='topic'),
    # 正则匹配，括号 表示正则中的组，Django会自动取值传递参数到views.topic方法中

    # 用于添加新主题的网页
    re_path(r'^new_topic/$',views.new_topic,name='new_topic'),

    # 用于添加新条目的页面
    re_path(r'new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),

    # 用于编辑条目的页面
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
]
app_name = 'learning_logs'
