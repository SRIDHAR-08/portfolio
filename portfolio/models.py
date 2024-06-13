from django.db import models
import datetime
import os

def FileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('profile_img/',new_filename)

def skill_img_FileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('profile_img/skill/',new_filename)

def project_img_FileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('profile_img/project/',new_filename)

def resume_img_FileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('profile_img/resume/',new_filename)

class profile_page(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField(default='null')
    Roll = models.CharField(max_length=60)
    experience = models.CharField(max_length=60)
    location = models.CharField(default='null',max_length=100)
    ph_number = models.CharField(default='null',max_length=10)
    gmail = models.EmailField(default='null')
    lnkedin = models.CharField(default='null',max_length=150)
    description = models.TextField(max_length=500)
    work_experience = models.TextField(max_length=500,default='null')
    SSLC = models.CharField(max_length=255)
    SSLC_year = models.CharField(max_length=255)
    SSLC_place = models.CharField(max_length=255,default='null')
    SSLC_percentage = models.CharField(max_length=255,default='null')
    HSC = models.CharField(max_length=255)
    HSC_year = models.CharField(max_length=255)
    HSC_place = models.CharField(max_length=255,default='null')
    HSC_percentage = models.CharField(max_length=255,default='null')
    collage_degree_s = models.CharField(max_length=255,default='null')
    collage_degree = models.CharField(max_length=255)
    collage_year = models.CharField(max_length=255)
    collage_place = models.CharField(max_length=255,default='null')
    collage_percentage = models.CharField(max_length=255,default='null')
    course = models.CharField(max_length=255)
    course_year = models.CharField(max_length=255)
    course_place = models.CharField(max_length=255,default='null')
    course_grade = models.CharField(max_length=255,default='null')
    profile_image = models.ImageField(upload_to=FileName,default='null')


    def __str__(self):
        return self .name
    
class resume(models.Model):
    profile_id = models.ForeignKey(profile_page,on_delete=models.CASCADE)
    resume = models.FileField(default='null',upload_to=resume_img_FileName)
    resume_photo1 = models.ImageField(default='null' ,upload_to=resume_img_FileName)
    resume_photo2 = models.ImageField(default='null',upload_to=resume_img_FileName)
    resume_photo3 = models.ImageField(default='null',upload_to=resume_img_FileName)
    resume_photo4 = models.ImageField(default='null',upload_to=resume_img_FileName)

class skill(models.Model):
    skill_image = models.ImageField(upload_to=skill_img_FileName,default='null')
    skill_name = models.CharField(max_length=100,default='NULL')

    def __str__(self):
        return self .skill_name

class project(models.Model):
    project_img = models.ImageField(upload_to=project_img_FileName)
    project_name = models.CharField(max_length=100)
    project_name_w_p = models.CharField(max_length=100,default='null')
    project_description = models.TextField(max_length=500)
    url_name_project = models.CharField(max_length=30)
    url_name_details = models.CharField(max_length=30)
    language1 = models.CharField(max_length=50 ,default='null')
    language2 = models.CharField(max_length=50 ,default='null')
    language3 = models.CharField(max_length=50 ,default='null')
    language4 = models.CharField(max_length=50 ,default='null')
    language5 = models.CharField(max_length=50 ,default='null')
    language6 = models.CharField(max_length=50 ,default='null')
    language7 = models.CharField(max_length=50 ,default='null')
    language8 = models.CharField(max_length=50 ,default='null')
    

    def __str__(self):
        return self .project_name
    
class contect(models.Model):
    name = models.CharField(max_length=50)
    gmail = models.EmailField(default='null')
    message = models.TextField(default='null',max_length=500)
    message_send_date = models.CharField(default='null',max_length=30)
    message_send_time = models.CharField(default='null',max_length=30)
    
