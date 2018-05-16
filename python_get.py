# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq

#下载
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url);

file_name = "C:/Users/Administrator/Desktop/github_python.txt"
with open(file_name,'w',encoding='utf-8') as file_object:
	for item in pq(r.content):
		info = pq(item).html()
		# ~ desc = pq(item).find('.inq').html()
		# ~ print (info+"\n")
		file_object.write(info+"\n")
