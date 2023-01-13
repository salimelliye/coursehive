from django.shortcuts import redirect, render, get_object_or_404
from urllib import request
from django.shortcuts import render
from .forms import LinkRequestForm
from .models import *
from django.conf import settings
from django.shortcuts import render
# Create your views here.



def home(request, *args, **kwargs):
  instructor = Instructor.objects.last()
  course = Course.objects.all()
  context = {
  'instructor':instructor,
  'course':course,
  }
  return render(request, 'home.html', context)


def publications(request, *args, **kwargs):
  context = {

  }
  return render(request, 'publications.html', context)


def course(request, course_Code):
    course = Course.objects.get(Code = course_Code)
    material = Material.objects.all().filter(Lecture__Course = course.id)
   
    instructor = Instructor.objects.all()
    context = {
    'form': LinkRequestForm,
    'course': course,
    'instructor': instructor,
    'material':material,
   
    }
    if request.POST:
      form = LinkRequestForm(request.POST, request.FILES)
      print(request.FILES)
      if form.is_valid():
        form.save()
    
    return render(request, 'course.html', context)




  



    



