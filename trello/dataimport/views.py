from pyexpat import model
from django.shortcuts import render, HttpResponse

from django.views import View

# Create your views here.


class HandInputView(View):
    #model
    #form_class = 
    #template

    def get(self, request, *args, **kwargs):
        print("get called on hand input")
        return HttpResponse("get called on hand input")
        pass

    def post(self, request, *args, **kwargs):
        print("post called on hand input")
        #form = self.form_class(request.POST)

        # if form.is_valid():
        #     ##process data here

        #     return HttpResponse
        return HttpResponse("post called on hand input")
        pass


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
    #form_class = 
    #template

    def get(self, request, *args, **kwargs):
        print("get called on File input")
        return HttpResponse("get called on file input")

    def post(self, request, *args, **kwargs):

        print("post called on file input")
        #form = self.form_class(request.POST)

        # if form.is_valid():
        #     ##process data here

        #     return HttpResponse
        return HttpResponse("post called on file input")
