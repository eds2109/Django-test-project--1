from django.contrib import admin
from instructors.models import Instructor, Position, Course

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    #fields = ['name', 'surname', 'email', 'position']
    exclude = ['date_of_birth']

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Position)
admin.site.register(Course)
# Register your models here.
