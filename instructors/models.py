from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Instructor(models.Model):

    name = models.CharField(verbose_name=u'Instructor Name', max_length=255, help_text='This is name')
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)

    courses = models.ManyToManyField(Course)
    is_active = models.BooleanField(default=True)

    position = models.ForeignKey(Position, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
