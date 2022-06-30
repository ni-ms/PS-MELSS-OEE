from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.entryPage, name = 'EntryPage'),
    path("inputValues", views.inputValues, name = 'InputValues'),
    path("displayPage", views.displayPage, name = 'DisplayPage'),
    path("getHistoricalData", views.getHistoricalData, name = 'GetHistoricalData'),
    path("displayHistoricalData", views.displayHistoricalData, name = 'DisplayhistoricalData'),
]
