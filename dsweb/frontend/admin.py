from django.contrib import admin
from .models import *
from django.utils.html import format_html
  
class MaterialGalleryInline(admin.TabularInline):
    model = Material
    list_display =['video',]
    extra = 1

class LectureAdmin(admin.ModelAdmin):
    inlines = [MaterialGalleryInline,]

class StudentDisplay(admin.ModelAdmin):
  list_display =['Name', 'LastName', 'IDNumber', 'Email', 'Approved']

class SectionDisplay(admin.ModelAdmin):
  list_display =['Title', 'CRN']


class EventDisplay(admin.ModelAdmin):
   list_display = ['Title', 'Day', 'Start_time', 'End_time',]


class InstructorDisplay(admin.ModelAdmin):
  def image_tag(self, obj):
      return format_html('<img src="{}" style="width:100px; height:110px;"/>'.format(obj.Image.url))
  list_display = ['Fullname', 'image_tag',]

class MyAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        ordering = {
            "Courses": 1,
            "Sections": 2,
            "Instructors": 3,
            "Lectures":4,
            "Materials":5,
            "Students":6,
            "Publications":7,
            "Publication Categories":8,
            "Scheduling":9,
        }
        app_dict = self._build_app_dict(request)
        # a.sort(key=lambda x: b.index(x[0]))
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list

mysite = MyAdminSite()
admin.site = mysite



# Register your models here.
admin.site.register(Course)
admin.site.register(Section, SectionDisplay)
admin.site.register(Instructor, InstructorDisplay)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Material)
admin.site.register(Student, StudentDisplay)
admin.site.register(Event, EventDisplay)
admin.site.register(Publication)
admin.site.register(PublicationCategories)

