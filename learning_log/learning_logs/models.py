from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	"""用户学习的主题"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text
		
class Entry(models.Model):
	"""有关某个主题的具体知识"""
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now=True)
    #auto_now=True：以后每次修改model都会自动更新为最后时间
    #auto_now_add=True：会在model对象第一次被创建时，将字段的值设置为创建时的时间，以后修改对象时，字段的值不会再更新
	
	class Meta:
		verbose_name_plural = 'entries'
		
	def __str__(self):
		"""返回模型的字符串表示"""
		if len(self.text) > 50:
			return self.text[:50] + "..."
			
		return self.text[:50]
