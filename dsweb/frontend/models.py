from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.db import models


# Create your models here.


class Course(models.Model):
    Title = models.CharField(max_length=100)
    Code = models.CharField(max_length=10 ,null=True,)
    About = models.TextField(null=True)
    Sections = models.ManyToManyField('Section')
    def __str__(self):
      return f"{self.Title}"
    
        
       

class Section(models.Model):
    Title = models.CharField(max_length=300)
    CRN = models.CharField(max_length=5)
    WhatsaapGroup =  models.URLField(u'Whatsaap Group',max_length = 200, null=True, blank=True)
    Syllabus = models.FileField( null=True)
    Instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
      return f"{self.Title}:{self.CRN}"

    


class Instructor(models.Model):
    Fullname = models.CharField(u'Full Name',max_length=300)
    Position = models.CharField(max_length=300, null=True, blank=True)
    Description =  models.TextField()
    Email = models.EmailField(max_length = 254, null=True)
    Image = models.ImageField()
    Cv = models.FileField( null=True)
    Address = models.CharField(max_length=300, null=True, blank=True)
    Tel = models.CharField(max_length=100, null=True, blank=True)
    Fax = models.CharField(max_length=50, null=True, blank=True)
    TwitterURL = models.URLField(u'Twitter URL', max_length = 200, null=True, blank=True)
    LinkdinURL = models.URLField(u'Linkdin URL', max_length = 200, null=True, blank=True)
    GithubURL = models.URLField(u'Github URL', max_length = 200, null=True, blank=True)
    

    def __str__(self):
      return f"{self.Fullname}"
    


class Lecture(models.Model):
  Title = models.IntegerField(u'Lecture Number')
  ShortDescription =  models.TextField(u'Short Description',)
  Course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True)
  Date = models.DateField(null=True)
  def __str__(self):
      return f"{self.Title}"
  


class Student(models.Model):
  Name = models.CharField(max_length=50)
  LastName = models.CharField(max_length=50)
  IDNumber = models.CharField(max_length=20)
  Email = models.EmailField(max_length = 254, null=True)
  Approved = models.BooleanField('Approved', default=False) 
  Section = models.ForeignKey('Section', on_delete=models.CASCADE, null=True, blank=True)
  
  def __str__(self):
      return f"{self.Name} {self.LastName}"
  def save(self, *args, **kwargs):
   if self.Approved == True:
      send_mail('Welcome Message',
      'Dear student note that your request to join the Whatsaap group of the section has been accepted. You are asked to join via the following link:',
      settings.EMAIL_HOST_USER,
      ['elie24saab@gmail.com'],
      fail_silently=False)
    
   super(Student, self).save(*args, **kwargs)
    
  

class Material(models.Model):
  Notes = models.FileField(blank=True)
  JavaFiles = models.FileField(blank=True)
  Videos = models.FileField(blank=True)
  Solution = models.FileField(u'Solution Keys',blank=True, null=True)
  Lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE, null=True, blank=True)
  def __str__(self):
      return f"Lecture {self.Lecture}'s Material"


class Event(models.Model):
    Title = models.CharField(max_length=100)
    Day = models.DateField(u'Day of the event', help_text=u'Day of the event', )
    Start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    End_time = models.TimeField(u'Final time', help_text=u'Final time')
    Notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
    Section = models.ForeignKey('Section', on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'
    