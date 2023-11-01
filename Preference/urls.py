from django.urls import path
from . import views
from .views import api_data

urlpatterns = [
    path('data/', views.data_list, name='data_list'),
    path('apidata/', api_data.as_view(), name='api_data'),

    path('intensity_chart/', views.intensity_chart, name='intensity_chart'),
    path('likelihood_chart/', views.likelihood_chart, name='likelihood_chart'),
    path('relevance_chart/', views.relevance_chart, name='relevance_chart'),
    path('year_intensity_chart/', views.year_intensity_chart, name='year_intensity_chart'),
    path('year_relevance_chart/', views.year_relevance_chart, name='year_relevance_chart'),
    path('year_likelihood_chart/', views.year_likelihood_chart, name='year_likelihood_chart'),
    path('country_chart/',views.country_chart,name='country_chart'),

]
