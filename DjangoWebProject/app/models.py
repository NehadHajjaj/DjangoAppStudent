"""
Definition of models.
"""

from django.db import models

# Create your models here.
class student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    studant_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    year_of_graduat = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    year_of_graduat = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    def __str__(self): 
      return self.studant_name 


class teacher(models.Model):
    teach_id = models.AutoField(primary_key=True)
    teach_name = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self): 
      return self.teach_name


class recommendation(models.Model):
    recom_num = models.AutoField(primary_key=True)
    teach_id = models.ForeignKey(teacher, on_delete=models.CASCADE)
    stu_id = models.ForeignKey(student, on_delete=models.CASCADE)

    def __str__(self): 
      return self.recom_num