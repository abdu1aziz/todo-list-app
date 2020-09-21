from django.urls import path, include


from . import views







urlpatterns = [
    path('', views.home, name='home'),
    path('mark-task-done/<int:id>', views.markDone, name='markDone'),
    path('mark-all-as-done/', views.makeAllAsDone, name='makeAllAsDone'),
    path('add-new-task/', views.addTask, name='addTask'),
]
