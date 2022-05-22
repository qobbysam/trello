from email import message
from pyexpat import model
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.core import serializers
from django.urls import reverse

import pickle

from .services import handle_user_file_input_post, handle_user_input_get, handle_user_input_post, handle_user_file_get
from .forms import UserFileUploadForm, UserHandInputForm
# Create your views here.


class HandInputView(LoginRequiredMixin,View):
    #model
    form_class = UserHandInputForm
    #template

    def get(self, request, *args, **kwargs):
        print("get called on hand input")

        objs, res = handle_user_input_get(request.user)
        if res:
            print('sucess')
            request.session['input_obj'] = serializers.serialize('json', objs)
            return HttpResponseRedirect("/")
        else:
            print('failed')
       
        return HttpResponseRedirect("/")
        

    def post(self, request, *args, **kwargs):
        print("post called on hand input")
        form = self.form_class(request.POST)

        if form.is_valid():
            ##process data here
            #print(form.age)
            res = handle_user_input_post(request.user, form=form)

            if res:
                messages.success(request, "creation successful")

                return HttpResponseRedirect("/")
            else:
                messages.error(request, "creation did not happen")
                return HttpResponseRedirect("/")
        else:

            messages.warning(request, "form submitted is not valid")

            return HttpResponseRedirect("/")
            


class DeviceInputView(View):
    #model
    #form_class = 
    #template

    def get(self, request, *args, **kwargs):
        print("get called on device input")
        return HttpResponse("get called on Device input")
        

    def post(self, request, *args, **kwargs):
        print("post called on device input")
        #form = self.form_class(request.POST)

        # if form.is_valid():
        #     ##process data here

        #     return HttpResponse
        return HttpResponse("post called on Device input")


class FileInputView(View):
        #model
    form_class = UserFileUploadForm
    #template

    def get(self, request, *args, **kwargs):
        print("get called on File input")

        objs, res = handle_user_file_get(request.user)
        if res:
            print('sucess')
            request.session['file_obj'] = serializers.serialize('json', objs)
            return HttpResponseRedirect("/")
        else:
            print('failed')
       
        return HttpResponseRedirect("/")

    def post(self, request, *args, **kwargs):

        print("post called on file input")
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
        #     ##process data here

            res = handle_user_file_input_post(request.user, form=form)

            if res:
                messages.success(request, "creation successful")

                return HttpResponseRedirect("/")
            else:
                messages.error(request, "creation not successful")

                return HttpResponseRedirect("/")

        else:
            messages.error(request, "form was not valid")
            return HttpResponseRedirect("/")
        #     return HttpResponse
        #return HttpResponse("post called on file input")
