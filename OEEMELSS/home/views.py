from django.shortcuts import render
# Create your views here.
from django.db import connection
from django.http import HttpRequest
from django.shortcuts import redirect, render, HttpResponse
from home.models import *
from django.contrib import messages

def entryPage(request):
    return render(request, 'LandingPage.html') #HttpResponse("this is homepage, or login") 

def inputValues(request):
    return render(request, 'CalculateOEE.html') #HttpResponse("this is where you input values")

def displayPage(request):
    return render(request, 'OEEOutput.html') #HttpResponse("this is where you show OEE value")

def getHistoricalData(request):
    return render(request, 'DisplayOEE.html') #HttpResponse("this is where you input machine and part id to display historical OEE value")

def displayHistoricalData(request):
    return render(request, 'OEEGraph.html') #HttpResponse("this is where you show historical OEE value for a given machine and part id")
