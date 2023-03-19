from django.urls import path
from expert_info.views import *

urlpatterns = [
    path('giris-yap', login, name="login"),
    path('cikis-yap', logout, name="logout"),
    path('', mainpage, name="mainpage"),
    path('adres/sehir-ekle', address_city, name="address_city"),
    path('adres/sehir-sil/id=<int:id>', address_city_delete, name="address_city_delete"),
    path('adres/ilce-ekle/il_id=<int:id>', address_county, name="address_county"),
    path('adres/ilce-sil/il_id=<int:city_id>/ilce_id=<int:county_id>', address_county_delete,
         name="address_county_delete"),
    path('adres/mahalle-ekle/il_id=<int:city_id>/ilce_id=<int:county_id>', address_neigbourhood,
         name="address_neigbourhood"),
    path('adres/mahalle-sil/il_id=<int:city_id>/ilce_id=<int:county_id>/mahalle_id=<int:id>',
         address_neighbourhood_delete, name="address_neighbourhood_delete"),
    path('rapor/ekle', add_rapor, name="add_rapor"),
    path('rapor/yakin-rapor', near_rapor, name="near_rapor"),
    path('tum-raporlar', all_rapor, name="all_rapor"),
    path('tum-raporlar/goruntule/id=<int:id>', show_rapor, name="show_rapor"),
    path('tum-raporlar/sil/id=<int:id>', delete_rapor, name="delete_rapor"),
    path('maaslar', maas, name="maas"),
    path('maaslar/sil/id=<int:id>', delete_maas, name="delete_maas"),
    path('maaslar/guncelle/id=<int:id>', update_maas, name="update_maas"),
    path('arac-kiralari', arac_kirasi, name="arac_kirasi"),
    path('arac-kiralari/sil/id=<int:id>', delete_arac_kirasi, name="delete_arac_kirasi"),
    path('arac-kiralari/guncelle/id=<int:id>', update_arac_kirasi, name="update_arac_kirasi"),
    path('primler', prim, name="prim"),
    path('primler/sil/id=<int:id>', delete_prim, name="delete_prim"),
    path('primler/guncelle/id=<int:id>', update_prim, name="update_prim"),
    path('prim-sorgu/<int:yil>/<int:ay>', get_json_prim, name="get_json_prim"),
    path('yapi-birim-maliyetleri', yapi_birim_maliyetleri, name="yapi_birim_maliyetleri"),
    path('yapi-birim-maliyetleri/sil/id=<int:id>', delete_yapi_birim_maliyeti, name="delete_yapi_birim_maliyeti"),
    path('yapi-birim-maliyetleri/guncelle/id=<int:id>', update_yapi_birim_maliyeti, name="update_yapi_birim_maliyeti"),
    path('imar-plani-onay-tarihleri', imar_plani_onay_tarihleri, name="imar_plani_onay_tarihleri"),
    path('imar-plani-onay-tarihleri/sil/id=<int:id>', delete_imarplani_onay_tarihi, name="delete_imarplani_onay_tarihi"),
    path('imar-plani-onay-tarihleri/guncelle/id=<int:id>', update_imar_plani_onay_tarihi, name="update_imar_plani_onay_tarihi"),

    path('ajax/load-counties/', load_ilceler, name='load_ilceler'),  # AJAX
    path('ajax/load-neighbourhoods/', load_mahalleler, name='load_mahalleler'),  # AJAX
]
