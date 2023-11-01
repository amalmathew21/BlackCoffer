from django.http import JsonResponse
from django.shortcuts import render
from .models import DataEntry

def data_list(request):
    data = DataEntry.objects.all()
    return render(request, 'datatemplates/data-list.html', {'data': data})



def api_data(request):
    data = DataEntry.objects.all().values()
    return JsonResponse({'data': list(data)})



import plotly.express as px
import pandas as pd

def intensity_chart(request):
    data = DataEntry.objects.all()
    data_list = list(data.values())
    df = pd.DataFrame(data_list)
    if not df.empty:
        fig = px.pie(df, x='country', y='intensity', title='Intensity Chart')
        return render(request, 'datatemplates/intensity_chart.html', {'chart': fig.to_html()})
    else:
        return render(request, 'datatemplates/no_data.html')

def likelihood_chart(request):
    data = DataEntry.objects.all()
    data_list = list(data.values())
    df = pd.DataFrame(data_list)
    if not df.empty:
        fig = px.bar(df, x='country', y='likelihood', title='Intensity Chart')
        return render(request, 'datatemplates/likelihood.html', {'chart': fig.to_html()})
    else:
        return render(request, 'datatemplates/no_data.html')

def relevance_chart(request):
    data = DataEntry.objects.all()
    data_list = list(data.values())
    df = pd.DataFrame(data_list)
    if not df.empty:
        fig = px.bar(df, x='country', y='relevance', title='Intensity Chart')
        return render(request, 'datatemplates/relevance_chart.html', {'chart': fig.to_html()})
    else:
        return render(request, 'datatemplates/no_data.html')

def year_relevance_chart(request):
    data = DataEntry.objects.all()
    data_list = list(data.values())
    df = pd.DataFrame(data_list)
    if not df.empty:
        fig = px.violin(df, x='end_year', y='relevance', title='Year vs. Intensity Violin Plot')
        return render(request, 'datatemplates/relevance_chart.html', {'chart': fig.to_html()})
    else:
        return render(request, 'datatemplates/no_data.html')

def year_intensity_chart(request):
    data = DataEntry.objects.all()
    data_list = list(data.values())
    df = pd.DataFrame(data_list)
    if not df.empty:
        fig = px.violin(df, x='end_year', y='intensity', title='Year vs. Intensity Violin Plot')



        return render(request, 'datatemplates/intensity_chart.html', {'chart': fig.to_html()})
    else:
        return render(request, 'datatemplates/no_data.html')

def year_likelihood_chart(request):
    data = DataEntry.objects.all()
    data_list = list(data.values())
    df = pd.DataFrame(data_list)
    if not df.empty:
        fig = px.violin(df, x='end_year', y='likelihood', title='Year vs. Intensity Violin Plot')
        return render(request, 'datatemplates/likelihood_chart.html', {'chart': fig.to_html()})
    else:
        return render(request, 'datatemplates/no_data.html')

def country_chart(request):
    data = DataEntry.objects.all()
    data_list = list(data.values())
    df = pd.DataFrame(data_list)
    if not df.empty:
        fig = px.pie(df, names='country', values='intensity', title='Country Chart')
        return render(request, 'datatemplates/country_chart.html', {'chart': fig.to_html()})

    else:
        return render(request, 'datatemplates/no_data.html')

