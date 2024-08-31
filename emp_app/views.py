
from django.shortcuts import redirect, render
from emp_app.models import*
from datetime import datetime
from django.http import  HttpResponse
from django.db.models import Q
# Create your views here.

def index(request):
  return render(request , 'index.html')

def all_emp(request):
  emp = Employee.objects.all()
  # print(emp)
  context ={
    'emp':emp
  }
  return render(request , 'view_all_emp.html',context)

def add_emp(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    selary = int(request.POST['selary'])
    bonus = int(request.POST['bonus'])
    contact_No = int(request.POST['contact_No'])
    dept = int(request.POST['dept'])
    role = int(request.POST['role'])
    
    new_emp = Employee(first_name = first_name, last_name=last_name, selary = selary, bonus = bonus, contact_No = contact_No, dept_id = dept, role_id = role, hire_date= datetime.now())
    
    new_emp.save()
    return redirect('/add_emp')
    
  return render(request , 'add_emp.html')

def remove_emp(request ,  emp_id = 0):
  if emp_id:
     try:
       emp_to_be_removed = Employee.objects.get(id = emp_id)
       emp_to_be_removed.delete()
       return HttpResponse('<h1>Employee Removed Successfully</h1>')
       
     except :
       return HttpResponse('Please Enter a Valid Emp  Id')
       
  emp = Employee.objects.all()
  # print(emp)
  context ={
    'emp':emp
  }
  return render(request , 'remove_emp.html',context)

def filter_emp(request):
  if request.method == 'POST':
    name=request.POST['name']
    dept=request.POST['dept']
    role=request.POST['role']
    emp = Employee.objects.all()
    
    if name:
      emp = emp.filter(Q(first_name__icontains = name)| Q(last_name__icontains = name))
    if dept:
      emp = emp.filter(dept__name = dept)
    if role:
      emp = emp.filter(role__name = role)
      
    context = {
      'emp' : emp 
   }
    return render(request, 'view_all_emp.html',context)
  
  elif request.method == 'GET':
     return render(request,'filter_emp.html')
   
  else:
    return HttpResponse('An Exception Occurred')
     
