from django.contrib import admin
from instructors.models import Instructor, Position, Course

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    fields = ['name', 'surname', 'email', 'date_of_birth', 'position', 'is_active']
    #exclude = ['date_of_birth']
    readonly_fields = ['is_active']
    raw_id_fields = ['position']

    save_as = True
    save_on_top = True

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Position)
admin.site.register(Course)
# Register your models here.
