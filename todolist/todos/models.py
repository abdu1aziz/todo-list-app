from django.db import models

# Create your models here.





class workList(models.Model):
	id      = models.AutoField(primary_key=True)

	user_id = models.IntegerField(null=False)
	task    = models.CharField(null=False, max_length=150)
	date    = models.DateTimeField(auto_now_add=True)
	is_done = models.BooleanField(default=False)
	
	def __str__(self):
		result = "User ID: %s | IS DONE # %s | Task Date: %s | Task Desc: %s" % (self.user_id, self.is_done, self.date, self.task)
		return result
	
	# class Meta:
	# 	verbose_name_plural = 'Sold Items'


# class shareTodoList(models.Model):
# 	id      = models.AutoField(primary_key=True)

# 	workList = models.ForeignKey(workList, on_delete=models.CASCADE)