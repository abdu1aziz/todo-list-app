



from django import forms
from .models import workList

class workListForm(forms.ModelForm):
	
	class Meta:
		model  = workList
		fields = {'task': '',}
		labels = {'task': '',}