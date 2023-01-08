from django.shortcuts import redirect, render, get_object_or_404
from urllib import request
from django.shortcuts import render
from .forms import LinkRequestForm
from .models import *
from django.conf import settings
from django.shortcuts import render
# Create your views here.



def home(request, *args, **kwargs):
  context = {

  }
  return render(request, 'home.html', context)


def course(request, course_Code, section_CRN):
    course = Course.objects.get(Code = course_Code)
    section = Section.objects.get(CRN=section_CRN)
    instructor = Instructor.objects.all()
    context = {
    'form': LinkRequestForm,
    'course': course,
    'section': section,
    'instructor': instructor,
   
    }
    if request.POST:
      form = LinkRequestForm(request.POST, request.FILES)
      print(request.FILES)
      if form.is_valid():
        form.save()
    
    return render(request, 'course.html', context)




  



    



