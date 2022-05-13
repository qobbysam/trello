from django.contrib import admin
from django.urls import path

from .views import HandInputView, DeviceInputView, FileInputView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hand/', HandInputView.as_view()),
    path('device/',DeviceInputView.as_view() ),
    path('file/', FileInputView.as_view()) ]