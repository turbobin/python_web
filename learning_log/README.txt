1,�������⻷����
���� D:\Program Files\java\eclipse-workspace\Python_Project\python_project\python_web\learning_log\ll_env\Scripts

����activate����

2,��װDjango��
pip install Django

3,��Django�д�����Ŀ��
django-admin.py startproject learning_log.
ĩβ�ĵ�������Ŀʹ�ú��ʵ�Ŀ¼�ṹ������ʡ��

4���������ݿ⣺
python manage.py migrate
������һ��SQLite���ݿ�(db.sqlite3�ļ�)

5������Django��������
python manage.py runserver

6.����Ӧ�ó���
python manage.py startapp learning_logs

7,����ģ�ͣ�
�޸�models.py

8,Ǩ����Ŀģ�ͣ�
ģ�͹������ݿ⣺
python manage.py makemigrations learning_logs

Ǩ�ƣ�
python manage.py migrate

�����ģ��ʱ���ظ�ִ�д˲��衣

9,Ϊ��վ���������û���
python manage.py createsuperuser
�����û��������䣬���뿪ʼ����
ccb_admin/ccb151517

10,�������վע��ģ��
��admin.py����ӣ�
from learning_logs.models immport Topic
admin.site.register(Topic)

11������ʽshell��������Ŀ
python manage.py shell		#��һ��shell�Ự

>>>from learning_logs.models import Topic
>>>Topic.objects.all()	#��ѯ����ʵ��������һ����ѯ���б�
>>>topics = Topic.objects.all()
>>>for topic in topics:
>>>    print(topic.id,topic)	#ÿ��������һ��ID����

>>> t = Topic.objects.get(id=1)
>>> t.text
'chess'
>>> t.date_added
from learning_logs.models import Topic
>>> t.entry_set.all()	#��ȡ���ض������������������Ŀ


