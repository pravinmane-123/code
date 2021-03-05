from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def display(request):
    a = '<h1> good morning </h1>'
    return HttpResponse(a)
