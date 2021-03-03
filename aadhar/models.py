from django.db import models

# Create your models here.
class aadhar_model(models.Model):
    aadhar_number=models.CharField(help_text="enter aadhar number",max_length=13,default='')
    name=models.CharField(help_text="ENTER name",max_length=40,default='')
    age=models.CharField(help_text="enter age",max_length=3,default='')
    

    def __str__(self):
         return self.aadhar_number+"-"+self.name
    