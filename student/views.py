from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello")

def About(request):
    return HttpResponse("My name is öMer")
