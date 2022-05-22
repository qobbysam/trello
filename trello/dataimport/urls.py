from django.contrib import admin
from django.urls import path

from .views import HandInputView, DeviceInputView, FileInputView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hand/', HandInputView.as_view(), name='handinput'),
    path('device/',DeviceInputView.as_view(), name='deviceinput' ),
    path('file/', FileInputView.as_view(), name='fileupload' ) ]