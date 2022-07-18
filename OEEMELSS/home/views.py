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
        TotalShiftTimeHr = float(request.POST.get('TotalShiftTimeHr'))
        TotalShiftTimeMin = float(request.POST.get('TotalShiftTimeMin'))
        PlannedDownTimeHr = float(request.POST.get('PlannedDownTimeHr'))
        PlannedDownTimeMin = float(request.POST.get('PlannedDownTimeMin'))
        AllDownTimeHr = float(request.POST.get('AllDownTimeHr'))
        AllDownTimeMin = float(request.POST.get('AllDownTimeMin'))
        AllStopTimeHr = float(request.POST.get('AllStopTimeHr'))
        AllStopTimeMin = float(request.POST.get('AllStopTimeMin'))
        ActualCycleTimeHr = float(request.POST.get('ActualCycleTimeHr'))
        ActualCycleTimeMin = float(request.POST.get('ActualCycleTimeMin'))
        TheoreticalCycleTimeHr = float(request.POST.get('TheoreticalCycleTimeHr'))
        TheoreticalCycleTimeMin = float(request.POST.get('TheoreticalCycleTimeMin'))
        ActualProcessingTimeHr = float(request.POST.get('ActualProcessingTimeHr'))
        ActualProcessingTimeMin = float(request.POST.get('ActualProcessingTimeMin'))
        TotalAmountProduced = float(request.POST.get('TotalAmountProduced'))
        DefectAmountProduced = float(request.POST.get('DefectAmountProduced'))        

        TotalShiftTime = (TotalShiftTimeHr*60) + TotalShiftTimeMin
        PlannedDownTime = (PlannedDownTimeHr*60) + PlannedDownTimeMin
        AllDownTime = (AllDownTimeHr*60) + AllDownTimeMin
        AllStopTime = (AllStopTimeHr*60) + AllStopTimeMin
        ActualCycleTime = (ActualCycleTimeHr*60) + ActualCycleTimeMin
        TheoreticalCycleTime = (TheoreticalCycleTimeHr*60) + TheoreticalCycleTimeMin
        ActualProcessingTime = (ActualProcessingTimeHr*60) + ActualProcessingTimeMin

        LoadingTime = TotalShiftTime-PlannedDownTime
        OperatingTime = LoadingTime - (AllDownTime + AllStopTime)
        Availability = (OperatingTime)/(LoadingTime)
        OperatingSpeedRate = (TheoreticalCycleTime)/(ActualCycleTime)
        NetOperatingRate = (ActualProcessingTime)/(OperatingTime)
        Performance = NetOperatingRate * OperatingSpeedRate
        Quality = (TotalAmountProduced - DefectAmountProduced)/TotalAmountProduced

        OEEValue = Availability * Quality * Performance * 100 * 100

    
    return render(request, 'Pages/CalculateOEE.html') #HttpResponse("this is where you input values")

def displayPage(request):
    return render(request, 'Pages/OEEOutput.html') #HttpResponse("this is where you show OEE value")

def getHistoricalData(request):
    return render(request, 'Pages/DisplayOEE.html') #HttpResponse("this is where you input machine and part id to display historical OEE value")

def displayHistoricalData(request):
    return render(request, 'Pages/OEEGraph.html') #HttpResponse("this is where you show historical OEE value for a given machine and part id")
