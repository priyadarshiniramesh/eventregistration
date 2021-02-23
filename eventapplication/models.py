from django.db import models

# Create your models here.

from django.contrib import admin

class Participant(models.Model):
    Name = models.CharField(max_length=100)
    Email= models.CharField(max_length=100)
    Phonenumber = models.IntegerField()
    Interest = models.CharField(max_length=100)
    Institutionname = models.CharField(max_length=100)


class ParticipantAdmin(admin.ModelAdmin):
    list_display=("Name","Email","Phonenumber", "Interest","Institutionname")
    