from django.db import models

# Create your models here.
class aadhar_model(models.Model):
    aadhar_number   =models.CharField(help_text="enter aadhar number",max_length=13,default='',blank=True)
    name            =models.CharField(help_text="ENTER name",max_length=40,default='')
    age             =models.CharField(help_text="enter age",max_length=3,default='')
    phone_number    =models.CharField(help_text="enter phone number",max_length=10,default=" ")
    voter_id        =models.CharField(help_text="Enter the voter id number",max_length=10,default='',blank=True)


    def __str__(self):
        if self.aadhar_number:
            return "Aadhar Number: "+self.aadhar_number+"-"+self.name
        else:
            return "VoterID : "+self.voter_id+"-"+self.name
    