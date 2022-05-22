from xml.dom.minidom import Identified
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserFileUpload(models.Model):
    FILE_CHOICES = [
        ('CSV', 'CSV'),
        ('JSON', 'JSON')
    ]
    file_name = models.CharField(max_length=30)
    file_type =models.CharField(max_length=4, choices=FILE_CHOICES)
    file = models.FileField(null=True, blank=True, upload_to="media/")
    file_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Type: %s, %s" %(self.file_type ,self.file_user)

class UserHandInput(models.Model):
    age = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
        return "input from %s, val %s" %(self.user, self.age)

class UserGadgetInfo(models.Model):
    GADGET_TYPE = [
        ('FB', 'FITBIT'),
        ('SW', 'SMARTWATCH')
    ]

    device_type = models.CharField(max_length=2, choices=GADGET_TYPE)
    api_key = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "From: %s, For: %s" %(self.device_type, self.user) 

class UserGagetData(models.Model):
    gagetinfo = models.ForeignKey(UserGadgetInfo, on_delete=models.CASCADE)
    apidata = models.CharField(max_length=30)

    def __str__(self) -> str:
        return "%s, data: %s" % (self.gagetinfo, self.apidata)
