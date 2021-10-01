from django.db import models

# Create your models here.
#class Positoin(models.Model):
class Instructor(models.Model):

    name = models.CharField(verbose_name=u'Instructor Name', max_length=255, help_text='This is name')
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)

    courses = models.CharField(null=True, max_length=255)
    is_active = models.BooleanField(default=True)

    position = models.CharField(max_length=1,
                                choices=(('i', 'Instructor'),
                                         ('a', 'Assistent')))

    def __str__(self):
        return self.name
