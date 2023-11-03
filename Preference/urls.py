from django.urls import path
from . import views
from .views import api_data

urlpatterns = [
    path('', views.homepage, name='home'),

    path('data/', views.data_list, name='data_list'),
    path('apidata/', api_data.as_view(), name='api_data'),

    path('likelihoodchart/', views.likelihoodChart, name='likelihoodchart'),
    path('relevancechart/', views.relevanceChart, name='relevancechart'),
    path('intensitychart/', views.intensityChart, name='intensitychart'),
    path('yearchart/', views.yearChart, name='yearchart'),
    path('countrychart/', views.countryChart, name='countrychart'),
    path('topicchart/', views.topicChart, name='topicchart'),
    path('regionchart/', views.regionChart, name='regionchart'),

]
