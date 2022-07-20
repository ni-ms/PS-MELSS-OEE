from django.contrib import admin
from django.urls import path
from home import views


from .views import get_data

urlpatterns = [
    path("admin/",admin.site.urls),

    path("dashboard/", views.dashboard, name = 'dashboard'),

    path("logout/", views.logoutPage, name = 'logout'),

    path("loginError/", views.loginErrorPage, name = 'loginError'),

    path("errorPage/", views.ErrorPage, name = '404error'),

    path("", views.entryPage, name = 'EntryPage'),

    path("inputValues/", views.inputValues, name = 'inputValues'),

    path("displayPage/", views.displayPage, name = 'displayPage'),

    path("getHistoricalData/", views.getHistoricalData, name = 'getHistoricalData'),
    
    path("displayHistoricalData/", views.displayHistoricalData, name = 'displayHistoricalData'),

    path("dataapi/", get_data, name='api-data'),

]
