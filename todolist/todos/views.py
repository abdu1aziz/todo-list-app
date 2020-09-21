from django.shortcuts import render

from .models import workList

# Create your views here.




def home(request):
	current_userID = request.user.id
	print("\n\nMY USER ID: %s\n\n" % (current_userID))
	works = workList.objects.filter(user_id=current_userID)

	context = {'works': works}
	return render(request, 'todos/index.html', context)



def markDone(request, id):
	current_userID = request.user.id
	pass