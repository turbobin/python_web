# -*- coding: utf-8 -*-
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

def write_info():
    print("\nSelect information about each repository..")
    file_name = "C:/Users/Administrator/Desktop/github_pyitems.txt"
    with open(file_name,'w',encoding='utf-8') as f_obj:
        for repo_dict in repo_dicts:
            f_obj.write("\nName:"+repo_dict["name"])
            f_obj.write("\nOwner:"+repo_dict["owner"]["login"])
            f_obj.write("\nStars:"+str(repo_dict["stargazers_count"]))
            f_obj.write("\nRepository:"+repo_dict["html_url"])
            f_obj.write("\nDescription:"+str(repo_dict["description"]))
            f_obj.write("\n")
            
    print("file created,view C:/Users/Administrator/Desktop/github_pyitems.txt")

#执行API调用，并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()
#处理结果
print(response_dict.keys())
# for key,value in response_dict.items():
#     print(key)

print("Total:",response_dict["total_count"])

#探索有关仓库的信息
repo_dicts =  response_dict["items"]
print("items counts:",len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))
# for key in repo_dict.keys():
#     print(key)
    
#提取项目具体信息，输出打印到文件中
# write_info()

# names, stars = [], []
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'lable':repo_dict['description'],    #在条形图中添加标签
        'xlink':repo_dict['html_url']    #在图表中添加可单击的链接
        }
    plot_dicts.append(plot_dict)
#     stars.append(repo_dict["stargazers_count"])
    
#数据可视化
my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add("", plot_dicts)
chart.render_to_file('python_repos.svg')
