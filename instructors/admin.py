from django.contrib import admin
from instructors.models import Instructor, Position, Course

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Position)
admin.site.register(Course)
# Register your models here.
