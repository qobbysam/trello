
#from dataclasses import fields
from django import forms 
from .models import UserFileUpload, UserGadgetInfo

class UserHandInputForm(forms.Form):
    age = forms.IntegerField(label="age")


class UserFileUploadForm(forms.ModelForm):
    class Meta:
        model = UserFileUpload
        fields = ['file_name', 'file_type', 'file']


class UserRegisterGadgetForm(forms.ModelForm):
    class Meta:
        model = UserGadgetInfo
        fields = ['device_type', 'api_key']


class UserGadgetConsumeForm(forms.Form):
    pk = forms.CharField(label="owner id")
    data = forms.CharField(label="data")