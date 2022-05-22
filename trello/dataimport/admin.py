from django.contrib import admin

from .models import UserHandInput, UserFileUpload
# Register your models here.

admin.site.register(UserHandInput)
admin.site.register(UserFileUpload)
