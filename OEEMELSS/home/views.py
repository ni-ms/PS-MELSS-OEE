from django.shortcuts import render
# Create your views here.
from django.db import connection
from django.http import HttpRequest
from django.shortcuts import redirect, render, HttpResponse
from home.models import *
from django.contrib import messages

def entryPage(request):
    return HttpResponse("this is homepage, or login") #render(request, 'entryPage.html')

def inputValues(request):
    return HttpResponse("this is where you input values")

def displayPage(request):
    return HttpResponse("this is where you show OEE value")

def getHistoricalData(request):
    return HttpResponse("this is where you input machine and part id to display historical OEE value")

def displayHistoricalData(request):
    return HttpResponse("this is where you show historical OEE value for a given machine and part id")
