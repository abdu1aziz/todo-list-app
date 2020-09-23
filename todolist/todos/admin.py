from django.contrib import admin

from .models import workList, shareTodoList


# Register your models here.


admin.site.register(workList)
admin.site.register(shareTodoList)