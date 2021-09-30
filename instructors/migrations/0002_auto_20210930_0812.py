# Generated by Django 3.2.7 on 2021-09-30 08:12

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
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(help_text='This is name', max_length=255, verbose_name='Instructor Name'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='surname',
            field=models.CharField(max_length=255),
        ),
    ]