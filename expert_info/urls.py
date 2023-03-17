from django.urls import path
from expert_info.views import *

urlpatterns = [
    path('giris-yap', login, name="login"),
    path('', mainpage, name="mainpage"),
    path('adres/sehir-ekle', address_city, name="address_city"),
    path('adres/sehir-sil/id=<int:id>', address_city_delete, name="address_city_delete"),
    path('adres/ilce-ekle/il_id=<int:id>', address_county, name="address_county"),
    path('adres/ilce-sil/il_id=<int:city_id>/ilce_id=<int:county_id>', address_county_delete, name="address_county_delete"),
    path('adres/mahalle-ekle/il_id=<int:city_id>/ilce_id=<int:county_id>', address_neigbourhood, name="address_neigbourhood"),
    path('adres/mahalle-sil/il_id=<int:city_id>/ilce_id=<int:county_id>/mahalle_id=<int:id>', address_neighbourhood_delete, name="address_neighbourhood_delete"),
]
