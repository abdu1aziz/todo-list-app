from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import workList

from .forms import workListForm
# Create your views here.



@login_required(login_url='login')
def home(request):
	workForm = workListForm()
	current_userID = request.user.id
	#print("\n\nMY USER ID: %s\n\n" % (current_userID))
	works 	 = workList.objects.filter(user_id=current_userID)
	is_done  = workList.objects.filter(user_id=current_userID).filter(is_done=True).count()
	not_done = workList.objects.filter(user_id=current_userID).filter(is_done=False).count()
	
	
	context = {'works': works, 'not_done': not_done, 'is_done': is_done, 'workForm': workForm}
	return render(request, 'todos/index.html', context)


@login_required(login_url='login')
def markDone(request, id):
	current_userID = request.user.id
	works = workList.objects.filter(user_id=current_userID).filter(id=id).exists()

	if works:
		check = workList.objects.filter(id=id).first()
		if check.is_done:
			workList.objects.filter(id=id).update(is_done=False)
			print("\n\nYOU ARE ALLOWED TO CHANGE THIS TASK!!\nTASK_ID: %s\n\n" % (id))
			return redirect('home')
		else:
			workList.objects.filter(id=id).update(is_done=True)
			return redirect('home')

	#print("THERE WAS AN UNEXPECTED ERROR!")
	return redirect('home')


@login_required(login_url='login')
def makeAllAsDone(request):
	current_userID = request.user.id
	works = workList.objects.filter(user_id=current_userID).exists()

	if works:
		check = workList.objects.filter(user_id=current_userID).update(is_done=True)
		return redirect('home')
	else:
		return redirect('home')


@login_required(login_url='login')
def addTask(request):
	current_userID = request.user.id
	works = workList.objects.filter(user_id=current_userID).exists()

	workForm = workListForm(request.POST)
	if works and request.method == "POST" and workForm.is_valid():
		task    = workForm.cleaned_data['task']
		workList(task=task, user_id=current_userID).save()

	workForm = workListForm()
	return redirect('home')


# ADD DELETE TASK FUNCTIONATLITY
# <a class="remove-item btn btn-default btn-xs pull-right" href="/mark-task-done/2">
#                                 <span class="glyphicon glyphicon-remove"></span>
#                             </a>