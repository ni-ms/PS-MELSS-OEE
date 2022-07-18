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
    if request.method == 'POST':
        MachineID = request.POST.get('MachineID')
        TotalShiftTimeHr = int(request.POST.get('TotalShiftTimeHr'))
        TotalShiftTimeMin = int(request.POST.get('TotalShiftTimeMin'))
        PlannedDownTimeHr = int(request.POST.get('PlannedDownTimeHr'))
        PlannedDownTimeMin = int(request.POST.get('PlannedDownTimeMin'))
        AllDownTimeHr = int(request.POST.get('AllDownTimeHr'))
        AllDownTimeMin = int(request.POST.get('AllDownTimeMin'))
        AllStopTimeHr = int(request.POST.get('AllStopTimeHr'))
        AllStopTimeMin = int(request.POST.get('AllStopTimeMin'))
        ActualCycleTimeHr = int(request.POST.get('ActualCycleTimeHr'))
        ActualCycleTimeMin = int(request.POST.get('ActualCycleTimeMin'))
        ActualOperationalTimeHr = int(request.POST.get('ActualOperationalTimeHr'))
        ActualOperationalTimeMin = int(request.POST.get('ActualOperationalTimeMin'))
        TheoreticalCycleTimeHr = int(request.POST.get('TheoreticalCycleTimeHr'))
        TheoreticalCycleTimeMin = int(request.POST.get('TheoreticalCycleTimeMin'))
        ActualProcessingTimeHr = int(request.POST.get('ActualProcessingTimeHr'))
        ActualProcessingTimeMin = int(request.POST.get('ActualProcessingTimeMin'))
        TotalAmountProduced = int(request.POST.get('TotalAmountProduced'))

        TotalShiftTime = (TotalShiftTimeHr*60) + TotalShiftTimeMin
        PlannedDownTime = (PlannedDownTimeHr*60) + PlannedDownTimeMin
        AllDownTime = (AllDownTimeHr*60) + AllDownTimeMin
        AllStopTime = (AllStopTimeHr*60) + AllStopTimeMin
        ActualCycleTime = (ActualCycleTimeHr*60) + ActualCycleTimeMin
        ActualOperationalTime = (ActualOperationalTimeHr*60) + ActualOperationalTimeMin
        TheoreticalCycleTime = (TheoreticalCycleTimeHr*60) + TheoreticalCycleTimeMin
        ActualProcessingTime = (ActualProcessingTimeHr*60) + ActualProcessingTimeMin

        
    
    return render(request, 'Pages/CalculateOEE.html') #HttpResponse("this is where you input values")

def displayPage(request):
    return render(request, 'Pages/OEEOutput.html') #HttpResponse("this is where you show OEE value")

def getHistoricalData(request):
    return render(request, 'Pages/DisplayOEE.html') #HttpResponse("this is where you input machine and part id to display historical OEE value")

def displayHistoricalData(request):
    return render(request, 'Pages/OEEGraph.html') #HttpResponse("this is where you show historical OEE value for a given machine and part id")
