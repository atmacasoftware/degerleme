from django.http import JsonResponse
from django.shortcuts import render
from address.models import *
# Create your views here.

def get_json_address_city_data(request):
    qs_val = list(Citys.objects.values())
    return JsonResponse({'data': qs_val})

def get_json_address_county_data(request, *args, **kwargs):
    selected_city = kwargs.get('id')
    obj_city = list(County.objects.filter(city_id=selected_city).values())
    return JsonResponse({'data': obj_city})

def get_json_address_neighbourhood_data(request, *args, **kwargs):
    selected_county = kwargs.get('id')
    obj_county = list(Neighbourhood.objects.filter(county_id=selected_county).values())
    return JsonResponse({'data': obj_county})
