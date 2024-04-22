from django.db import models

# Create your models here.
class feedback(models.Model):
    course=models.CharField(max_length=100,default="")
    section=models.CharField(max_length=100,default="")
    batch=models.CharField(max_length=100, default="")
    semester=models.CharField(max_length=100,default="")
    Feedback=models.CharField(max_length=100 ,default="")
    grading=models.CharField(max_length=100,default="")
