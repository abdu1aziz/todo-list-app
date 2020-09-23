



from django import forms
from .models import workList, shareTodoList

class workListForm(forms.ModelForm):
	
	class Meta:
		model  = workList
		fields = {'task': '',}
		labels = {'task': '',}

class shareTodoListForm(forms.ModelForm):


	class Meta:
		model  = shareTodoList
		fields = '__all__'
		labels = {'workList': 'Select Task',  'userInfo':'Share With', }
		