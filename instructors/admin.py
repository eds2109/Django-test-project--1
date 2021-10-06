from django.contrib import admin
from django.db import models
from instructors.models import Instructor, Position, Course
from django.forms import widgets

class InstructorInline(admin.StackedInline):
    model = Instructor
    fields = ['name']

class PositionAdmin(admin.ModelAdmin):
    inlines = [InstructorInline]

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    #fields = ['name', 'surname', 'email', 'date_of_birth', 'position', 'is_active',]
    #exclude = ['date_of_birth']
    readonly_fields = ['is_active']
    raw_id_fields = ['position']

    save_as = True
    save_on_top = True


    fieldsets = [
        (None,                {'fields': ['name', 'surname']}),
        ('Other information', {'fields': ['email', 'date_of_birth', 'position', 'is_active'],
                               'classes': ['collapse']}),
    ]

    formfield_overrides = {
        models.DateField: {'widget': widgets.TextInput}
    }

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Course)
# Register your models here.
