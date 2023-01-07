from django.contrib import admin
from Employees.models import Employeejobmap

from .models import Job

class EmployeeInLine(admin.TabularInline):
    model = Employeejobmap

    def get_readonly_fields(self, request, *args, **kwargs):

         if request.user.is_superuser:
            return []

         else:
            return ('employee',)


class JobAdmin(admin.ModelAdmin):
    exclude = ('creater',)
    list_display = ('Designation', 'creater',)
    inlines = (EmployeeInLine,)

    def get_queryset(self, request, *args, **kwargs):

        if request.user.is_superuser:
            return Job.objects.all()

        else:
            return Job.objects.filter(creater = request.user)
        


    def get_list_display(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return ('Designation', 'creater',)

        else:
            return('Designation', )



    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # assign the creater only on creation and not update
            obj.creater = request.user
            obj.save()



admin.site.register(Job, JobAdmin)





