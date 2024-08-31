from django.db import models


# Create your models here.

class Department(models.Model):
   name = models.CharField(max_length = 100)
   location = models.CharField(max_length = 100)
   
   def __str__(self) -> str:
      return self.name

class Role(models.Model):
   name = models.CharField(max_length = 100)
   def __str__(self) -> str:
      return self.name
  
class Employee(models.Model):
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)
  dept = models.ForeignKey(Department ,on_delete = models.CASCADE,blank=True,null=True)
  selary = models.IntegerField(default = 0)
  bonus = models.IntegerField(default = 0)
  role = models.ForeignKey(Role , on_delete = models.CASCADE,blank=True,null=True)
  contact_No = models.IntegerField(default = 0)
  hire_date = models.DateField(blank=True,null=True)
  
  def __str__(self) -> str:
    return "%s %s %s" %(self.first_name,self.last_name,self.contact_No)