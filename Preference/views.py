from django.shortcuts import render, redirect
from .models import DataEntry
from rest_framework import generics
from .serializers import DataEntrySerializer
from django.db.models import IntegerField

from django.db.models import Count



def homepage(request):
    return render(request,'main/Home.html')



def data_list(request):
    data = DataEntry.objects.all()
    return render(request, 'datatemplates/data-list.html', {'data': data})



class api_data(generics.ListAPIView):
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer



def likelihoodChart(request):
    data = (
        DataEntry.objects
        .values('likelihood')
        .annotate(count=Count('likelihood', output_field=IntegerField()))
    )

    likelihood_values = [float(entry['likelihood']) for entry in data]
    count_values = [entry['count'] for entry in data]

    context = {
        'likelihood_values': likelihood_values,
        'count_values': count_values,
    }

    return render(request, 'datatemplates/likelihood.html', context)


def relevanceChart(request):
    data = (
        DataEntry.objects
        .values('relevance')
        .annotate(count=Count('relevance', output_field=IntegerField()))
    )

    relevance_values = [float(entry['relevance']) for entry in data]
    count_values = [entry['count'] for entry in data]

    context = {
        'relevance_values': relevance_values,
        'count_values': count_values,
    }

    return render(request, 'datatemplates/relevance.html', context)

def intensityChart(request):
    data = (
        DataEntry.objects
        .values('intensity')
        .annotate(count=Count('intensity', output_field=IntegerField()))
    )

    intensity_values = [float(entry['intensity']) for entry in data]
    count_values = [entry['count'] for entry in data]

    context = {
        'intensity_values': intensity_values,
        'count_values': count_values,
    }

    return render(request, 'datatemplates/intensity.html', context)

def yearChart(request):
    data = (
        DataEntry.objects
        .values('end_year')
        .annotate(count=Count('end_year', output_field=IntegerField()))
    )

    year_values = [entry['end_year'] for entry in data]
    count_values = [entry['count'] for entry in data]

    context = {
        'year_values': year_values,
        'count_values': count_values,
    }

    return render(request, 'datatemplates/year.html', context)

def countryChart(request):
    data = (
        DataEntry.objects
        .values('country')
        .annotate(count=Count('country', output_field=IntegerField()))
    )

    country_values = [entry['country'] for entry in data]

    count_values = [entry['count'] for entry in data]

    context = {
        'country_values': country_values,
        'count_values': count_values,
    }

    return render(request, 'datatemplates/country.html', context)

def topicChart(request):
    data = (
        DataEntry.objects
        .values('topic')
        .annotate(count=Count('topic', output_field=IntegerField()))
    )

    topic_values = [entry['topic'] for entry in data]
    count_values = [entry['count'] for entry in data]

    context = {
        'topic_values': topic_values,
        'count_values': count_values,
    }

    return render(request, 'datatemplates/topic.html', context)

def regionChart(request):
    data = (
        DataEntry.objects
        .values('region')
        .annotate(count=Count('region', output_field=IntegerField()))
    )

    region_values = [entry['region'] for entry in data]
    count_values = [entry['count'] for entry in data]

    context = {
        'region_values': region_values,
        'count_values': count_values,
    }

    return render(request, 'datatemplates/region.html', context)

