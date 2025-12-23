
from django.db import models
from django.contrib.auth.models import User

from allauth.socialaccount.models import SocialAccount



class employee_profile(models.Model):

    login_reference=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='imagaes/',null=True) 


    name=models.CharField(max_length=150,null=True)
    professional=models.CharField(max_length=150,null=True,default="you are  professional")
    email=models.CharField(max_length=150,null=True)
    number=models.CharField(max_length=10,null=True)
    location=models.CharField(max_length=200,null=True)
    skills=models.CharField(max_length=200,null=True)
   
    work_experience = models.CharField(max_length=1000, blank=True, null=True)
    education = models.CharField(max_length=1000, blank=True, null=True)
    project = models.CharField(max_length=1000, blank=True, null=True)

 



class job_list(models.Model):
    
    social_account = models.OneToOneField(SocialAccount,on_delete=models.CASCADE,related_name='job',
        null=True,
        blank=True)

    #company_logo = models.ImageField(upload_to='company_logo/',null=False, blank=False)
    Company=models.CharField(max_length=250,null=True,blank=False)
    job_name=models.CharField(max_length=150,null=True,blank=False)
    Location=models.CharField(max_length=500,null=True,blank=False)
    Type=models.CharField(max_length=150,null=True,blank=False)
    content=models.CharField(max_length=15000,null=True,blank=False)
    Industry=models.CharField(max_length=150,null=True,blank=False)
    Company_Size=models.CharField(max_length=150,null=True,blank=False)
    Experience=models.CharField(max_length=150,null=True,blank=False)
    Skills=models.CharField(max_length=150,null=True,blank=False)
    Description=models.CharField(max_length=15000,null=True,blank=False)
    Website=models.CharField(max_length=150,null=True,blank=False)


    

