1,激活虚拟环境：
进入 D:\Program Files\java\eclipse-workspace\Python_Project\python_project\python_web\learning_log\ll_env\Scripts

运行activate命令

2,安装Django：
pip install Django

3,在Django中创建项目：
django-admin.py startproject learning_log.
末尾的点让新项目使用合适的目录结构，不可省略

4，创建数据库：
python manage.py migrate
创建了一个SQLite数据库(db.sqlite3文件)

5，开启Django服务器：
python manage.py runserver

6.创建应用程序：
python manage.py startapp learning_logs

7,创建模型：
修改models.py

8,迁移项目模型：
模型关联数据库：
python manage.py makemigrations learning_logs

迁移：
python manage.py migrate

添加新模型时需重复执行此步骤。

9,为网站创建超级用户：
python manage.py createsuperuser
输入用户名，邮箱，密码开始创建
ccb_admin/ccb151517

10,向管理网站注册模型
打开admin.py，添加：
from learning_logs.models immport Topic
admin.site.register(Topic)

11，交互式shell，测试项目
python manage.py shell		#打开一个shell会话

>>>from learning_logs.models import Topic
>>>Topic.objects.all()	#查询所有实例，返回一个查询集列表
>>>topics = Topic.objects.all()
>>>for topic in topics:
>>>    print(topic.id,topic)	#每个主题有一个ID属性

>>> t = Topic.objects.get(id=1)
>>> t.text
'chess'
>>> t.date_added
from learning_logs.models import Topic
>>> t.entry_set.all()	#获取与特定主题相关联的所有条目

12.Django2.0关联表必填on_delete参数
一对多(ForeignKey)
一对一(oneToOneField)
on_delete参数的各个值的含义:
on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
# models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
# models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
on_delete=models.SET,         # 删除关联数据,
 a. 与之关联的值设置为指定值,设置：models.SET(值)
 b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)
 