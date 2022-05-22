"""trello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from dataimport.forms import UserFileUploadForm
from dataimport.forms import UserRegisterGadgetForm


##Default Route

class HomeRoute(TemplateView):
    template_name = 'home.html'

    form = UserFileUploadForm

    gaget_form = UserRegisterGadgetForm
    
    def get_context_data(self, *args, **kwargs):
        context = super(HomeRoute, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        context['gaget_form'] = self.gaget_form
        
        return context
##api routes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('imports/', include('dataimport.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    path('', HomeRoute.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
