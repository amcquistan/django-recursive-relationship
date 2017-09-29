
# hrmgmt/views.py
from django.shortcuts import render

from .models import Employee

def index(request):
    employees = Employee.objects.order_by('id').all()
    context = {'employees': employees}
    return render(request, 'hrmgmt/index.html', context)
