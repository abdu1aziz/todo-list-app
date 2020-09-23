from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class workList(models.Model):
	id      = models.AutoField(primary_key=True)

	user_id = models.IntegerField(null=False)
	task    = models.CharField(null=False, max_length=150)
	date    = models.DateTimeField(auto_now_add=True)
	is_done = models.BooleanField(default=False)
	
	def __str__(self):
		#result = "User ID: %s | IS DONE # %s | Task Date: %s | Task Desc: %s" % (self.user_id, self.is_done, self.date, self.task)
		result = "%s" % (self.task)
		return result
	
	# class Meta:
	# 	verbose_name_plural = 'Sold Items'


class shareTodoList(models.Model):
	id       = models.AutoField(primary_key=True)
	workList = models.ForeignKey(workList, on_delete=models.DO_NOTHING)
	userInfo = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	date	 = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		result = "TASK ID: %s | OWNER: %s | SHARED TO: %s | TASK: %s | SHARE DATE: %s " % (self.workList.id, self.workList.user_id, self.userInfo.id, self.workList.task, self.date)
		return result



