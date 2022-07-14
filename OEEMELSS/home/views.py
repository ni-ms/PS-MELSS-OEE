from django.shortcuts import render
# Create your views here.
from django.db import connection
from django.http import HttpRequest
from django.shortcuts import redirect, render, HttpResponse
from home.models import *
from django.contrib import messages

def entryPage(request):
    return render(request, 'LandingPage.html') #HttpResponse("this is homepage, or login") 

def dashboard(request):
    return render(request, 'Pages/HomePage.html')

def logoutPage(request):
    return render(request,'Pages/LogoutPage.html')

def loginErrorPage(request):
    return render(request,'Pages/401Page.html')

def ErrorPage(request):
    return render(request,'Pages/404Page.html')

def inputValues(request):
    return render(request, 'Pages/CalculateOEE.html') #HttpResponse("this is where you input values")

def displayPage(request):
    return render(request, 'Pages/OEEOutput.html') #HttpResponse("this is where you show OEE value")

def getHistoricalData(request):
    return render(request, 'Pages/DisplayOEE.html') #HttpResponse("this is where you input machine and part id to display historical OEE value")

def displayHistoricalData(request):
    return render(request, 'Pages/OEEGraph.html') #HttpResponse("this is where you show historical OEE value for a given machine and part id")
