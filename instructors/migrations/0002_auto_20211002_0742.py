# Generated by Django 3.2.7 on 2021-10-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='course',
        ),
        migrations.AddField(
            model_name='instructor',
            name='courses',
            field=models.ManyToManyField(to='instructors.Course'),
        ),
    ]
