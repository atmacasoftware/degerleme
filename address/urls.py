from django.urls import path
from address.views import *

urlpatterns = [
    path('city-county-json/', get_json_address_city_data, name="city-json"),
    path('city-county-json/<int:id>/', get_json_address_county_data, name='county-json'),
    path('county-neighbourhood-json/<int:id>/', get_json_address_neighbourhood_data, name='county-json'),
]
