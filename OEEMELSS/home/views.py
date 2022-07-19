from collections import defaultdict
from re import M
from django.shortcuts import render
# Create your views here.
from django.db import connection
from django.http import HttpRequest
from django.shortcuts import redirect, render, HttpResponse
from home.models import *
from django.contrib import messages

def entryPage(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        PW = request.POST.get("PW")

        post = AuthenticateUser.objects.filter(UserName = Username)

        if post.exists():
            return redirect(request, '/dashboard')
        else:
            return redirect(request, '/loginErrorPage')
    
    return render(request, 'LandingPage.html') #HttpResponse("this is homepage, or login") 

def dashboard(request):
    return render(request, 'Pages/HomePage.html')

def logoutPage(request):
    return render(request,'Pages/LogoutPage.html')

def loginErrorPage(request):
    return render(request,'Pages/401Page.html')

def ErrorPage(request):
    return render(request,'Pages/404Page.html')

def inputValues(request): # complete
    if request.method == 'POST':
        MachineID = request.POST.get('MachineID') # Enter in DB
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
        Availability = ((OperatingTime)/(LoadingTime)) * 100 # Enter in DB
        OperatingSpeedRate = (TheoreticalCycleTime)/(ActualCycleTime)
        NetOperatingRate = (ActualProcessingTime)/(OperatingTime)
        Performance = (NetOperatingRate * OperatingSpeedRate) * 100 # Enter in DB
        Quality = ((TotalAmountProduced - DefectAmountProduced)/TotalAmountProduced) * 100 # Enter in DB

        OEEValue = (Availability * Quality * Performance) / 10000
        print(OEEValue, Availability, Quality, Performance)

        Block = []
        Min = min(Availability,Performance,Quality)
        if Min != 100.0 and Min != 0:
            if Min == Availability:
                Block.append("Try to reduce Planned stops")
                Block.append("Try to reduce Unplanned stops")

            if Min == Performance:
                Block.append("Reduce Micro stops")
                Block.append("Increase cycle speed")
            if Min == Quality:
                Block.append("Reduce Start-up rejects")
                Block.append("Reduce Production rejects")
        elif Min == 100.0:
            Block.append("Machine is Perfect")
    
        elif Min == 0.0:
            Block.append("Machine Broken")

    

        # Enter mongo Raw commands here, done 
        post = OEEValues()
        post.machineid = MachineID
        post.oeevalue = OEEValue
        post.Avalue = Availability
        post.Pvalue = Performance
        post.Qvalue = Quality
        post.save()

        # End mongo Raw commands here
        request.session['project_details'] = {"id":MachineID, "OEEValue":OEEValue, "A":Availability,"P":Performance,"Q":Quality, "Block":Block}

        return redirect('/displayPage')

    
    return render(request, 'Pages/CalculateOee.html') #HttpResponse("this is where you input values")


def displayPage(request): # complete
    dict = request.session.get('project_details')
    MachineID = dict["id"]
    OEEValue = dict["OEEValue"]
    A = dict["A"]
    P = dict["P"]
    Q = dict["Q"]
    Block = dict["Block"]

    return render(request, 'Pages/OEEOutput.html', dict) #HttpResponse("this is where you show OEE value")

def getHistoricalData(request):
    dict = {"id":None}
    if request.method == "POST":
        MachineID = request.POST.get('MachineID')
        m1 = float(MachineID)
        if m1 == 0.0:
            #something
            print()
            post = OEEValues.objects.all()

        else:
            #something
            print()
            post = OEEValues.objects.all()
            post = OEEValues.objects.filter(machineid = MachineID)
            

        dict = {"id":post}
    
    
    return render(request, 'Pages/DisplayOEE.html', dict) #HttpResponse("this is where you input machine and part id to display historical OEE value")

def displayHistoricalData(request):
    return render(request, 'Pages/OEEGraph.html') #HttpResponse("this is where you show historical OEE value for a given machine and part id")
