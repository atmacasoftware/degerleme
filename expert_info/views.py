import datetime

from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from address.models import Citys, County, Neighbourhood
from user_accounts.models import User
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from expert_info.forms import *
import math
import folium


# Create your views here.

def login(request):
    try:
        if request.user.is_authenticated:
            messages.success(request, 'Giriş yapıldı')
            return redirect('mainpage')
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_obj = User.objects.filter(email=email)
            if not user_obj.exists():
                messages.error(request, 'Bu kullanıcı mevcut değil.')
                return redirect('login')

            user_obj = authenticate(email=email, password=password)
            if (user_obj and user_obj.is_superuser) or (user_obj and user_obj.is_staff):
                auth_login(request, user_obj)
                return redirect('mainpage')

            messages.warning(request, 'Yanlış şifre!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render(request, 'auth/login.html')
    except Exception as e:
        print(e)


@login_required(login_url="/giris-yap")
def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required(login_url="/giris-yap")
def mainpage(request):
    context = {}
    today = datetime.datetime.now()
    report_count = RaporEkle.objects.all().count()

    primler = Prim.objects.filter(user=request.user, yil=str(today.year), ay=str(today.month))
    total_prim = 0
    for p in primler:
        total_prim += (p.prim) * 0.1

    kazanc = 0

    maaslar = Maas.objects.filter(user=request.user)
    arac_kira = AracKira.objects.filter(user=request.user)

    for m in maaslar:
        kazanc += m.maas

    for a in arac_kira:
        kazanc += a.kira

    context.update({
        'report_count': report_count,
        'total_prim': total_prim,
        'kazanc': kazanc,
    })

    return render(request, 'pages/mainpage.html', context)


@login_required(login_url="/giris-yap")
def address_city(request):
    context = {}
    citys = Citys.objects.all()
    context.update({'citys': citys})

    if 'city_add' in request.POST:
        name = request.POST.get('name', None)
        if name is not None:
            data = Citys.objects.create(name=name)
            data.save()
            messages.success(request, 'Şehir başarıyla eklendi!')
            return redirect('address_city')
        else:
            messages.warning(request, 'Şehir adı boş olamaz!')
            return redirect('address_city')

    if 'city_update' in request.POST:
        update_name = request.POST.get('update_name', None)
        city_id = request.POST.get('city_id', None)

        if update_name is not None and city_id is not None:
            data = Citys.objects.get(id=city_id)
            data.name = update_name
            update_time = timezone.now()
            data.updated_at = update_time
            data.save()
            messages.success(request, 'Şehir başarıyla güncellendi!')
            return redirect('address_city')
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('address_city')

    return render(request, 'pages/address.html', context)


@login_required(login_url="/giris-yap")
def address_city_delete(request, id):
    city = Citys.objects.get(id=id)
    city.delete()
    messages.success(request, 'Şehir başarıyla silindi!')
    return redirect('address_city')


@login_required(login_url="/giris-yap")
def address_county(request, id):
    context = {}
    city = Citys.objects.get(id=id)
    context.update({'city': city})
    counties = County.objects.filter(city_id=id)
    context.update({'counties': counties})

    if 'county_add' in request.POST:
        name = request.POST.get('name', None)
        if name is not None:
            data = County.objects.create(name=name, city_id=id)
            data.save()
            messages.success(request, 'İlçe başarıyla eklendi!')
            return redirect('address_county', id)
        else:
            messages.warning(request, 'İlçe adı boş olamaz!')
            return redirect('address_county', id)

    if 'county_update' in request.POST:
        update_name = request.POST.get('update_name', None)
        county_id = request.POST.get('county_id', None)

        if update_name is not None and county_id is not None:
            data = County.objects.get(id=county_id)
            data.name = update_name
            update_time = timezone.now()
            data.updated_at = update_time
            data.save()
            messages.success(request, 'İlçe başarıyla güncellendi!')
            return redirect('address_county', id)
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('address_county', id)

    return render(request, 'pages/address_county.html', context)


@login_required(login_url="/giris-yap")
def address_county_delete(request, city_id, county_id):
    county = County.objects.get(id=county_id)
    county.delete()
    messages.success(request, 'İlçe başarıyla silindi!')
    return redirect('address_county', city_id)


@login_required(login_url="/giris-yap")
def address_neigbourhood(request, city_id, county_id):
    context = {}
    city = Citys.objects.get(id=city_id)
    county = County.objects.get(id=county_id)
    context.update({'city': city, 'county': county})
    neig = Neighbourhood.objects.filter(county_id=county_id)
    context.update({'neig': neig})

    if 'neig_add' in request.POST:
        name = request.POST.get('name', None)
        if name is not None:
            data = Neighbourhood.objects.create(name=name, city_id=city_id, county_id=county_id)
            data.save()
            messages.success(request, 'Mahalle başarıyla eklendi!')
            return redirect('address_neigbourhood', city_id, county_id)
        else:
            messages.warning(request, 'Mahalle adı boş olamaz!')
            return redirect('address_neigbourhood', city_id, county_id)

    if 'neig_update' in request.POST:
        update_name = request.POST.get('update_name', None)
        neig_id = request.POST.get('neig_id', None)

        if update_name is not None and neig_id is not None:
            data = Neighbourhood.objects.get(id=neig_id)
            data.name = update_name
            update_time = timezone.now()
            data.updated_at = update_time
            data.save()
            messages.success(request, 'Mahalle başarıyla güncellendi!')
            return redirect('address_neigbourhood', city_id, county_id)
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('address_neigbourhood', city_id, county_id)

    return render(request, 'pages/address_neighbourhood.html', context)


@login_required(login_url="/giris-yap")
def address_neighbourhood_delete(request, city_id, county_id, id):
    neig = Neighbourhood.objects.get(id=id)
    neig.delete()
    messages.success(request, 'Mahalle başarıyla silindi!')
    return redirect('address_neigbourhood', city_id, county_id)


@login_required(login_url="/giris-yap")
def add_rapor(request):
    context = {}
    form = RaporEkleAddForm(data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    if 'add_reports' in request.POST:
        user = request.user
        rapor_no = request.POST.get('rapor_no')
        il = request.POST.get('il')
        ilce = request.POST.get('ilce')
        mahalle = request.POST.get('mahalle')
        ada = request.POST.get('ada')
        parsel = request.POST.get('parsel')
        enlem = request.POST.get('enlem')
        boylam = request.POST.get('boylam')
        ana_tasinmaz_nitelik = request.POST.get('ana_tasinmaz_nitelik')
        nitelik = request.POST.get('nitelik')
        yuzolcum = request.POST.get('yuzolcum')
        deger = request.POST.get('deger')
        kat = request.POST.get('kat')
        oda_sayisi = request.POST.get('oda_sayisi')
        isinma_sistemi = request.POST.get('isinma_sistemi')
        deger_tarihi = request.POST.get('deger_tarihi')
        asansor = request.POST.get('asansor')
        otopark = request.POST.get('otopark')
        guvenlik = request.POST.get('guvenlik')
        yapi_kalitesi = request.POST.get('yapi_kalitesi')
        yapim_yili = request.POST.get('yapim_yili')
        dosya_konumu = request.POST.get('dosya_konumu')

        data = RaporEkle.objects.create(user=user, rapor_no=rapor_no, il_id=il, ilce_id=ilce, mahalle_id=mahalle,
                                        ada=ada, parsel=parsel, enlem=enlem, boylam=boylam,
                                        ana_tasinmaz_nitelik=ana_tasinmaz_nitelik, nitelik=nitelik, yuzolcum=yuzolcum,
                                        deger=deger,
                                        kat=kat, oda_sayisi=oda_sayisi, isinma_sistemi=isinma_sistemi,
                                        deger_tarihi=deger_tarihi, asansor=asansor, otopark=otopark, guvenlik=guvenlik,
                                        yapi_kalitesi=yapi_kalitesi, yapim_yili=yapim_yili, dosya_konumu=dosya_konumu)
        data.save()

        messages.success(request, 'Rapor başarıyla silindi!')
        return redirect('add_rapor')

    return render(request, 'pages/add_reports.html', context)


@login_required(login_url="/giris-yap")
def all_rapor(request):
    context = {}
    reports = RaporEkle.objects.all()
    context.update({'reports': reports})
    return render(request, 'pages/all_reports.html', context)


@login_required(login_url="/giris-yap")
def show_rapor(request, id):
    context = {}
    report = RaporEkle.objects.get(id=id)
    context.update({'report': report})
    form = RaporEkleUpdateForm(instance=report, data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    map = folium.Map(location=[report.enlem, report.boylam], zoom_start=15)
    folium.Marker([report.enlem, report.boylam], popup=report.rapor_no, draggable=False).add_to(map)
    map = map._repr_html_()
    context.update({
        'map': map
    })

    if 'update_report' in request.POST:
        if form.is_valid():
            data = form.save(commit=False)
            update_time = timezone.now()
            data.updated_at = update_time
            data.save()
            messages.success(request, 'Rapor başarıyla güncellendi!')
            return redirect('show_rapor', id)

    return render(request, 'pages/show_report.html', context)


@login_required(login_url="/giris-yap")
def delete_rapor(request, id):
    report = RaporEkle.objects.get(id=id)
    report.delete()
    return redirect('all_rapor')


@login_required(login_url="/giris-yap")
def near_rapor(request):
    context = {}
    all_reports = RaporEkle.objects.all()
    query_reports = []

    if 'query' in request.POST:
        enlem = request.POST.get('enlem', None)
        boylam = request.POST.get('boylam', None)
        mesafe = request.POST.get('mesafe', None)

        map = folium.Map(location=[enlem, boylam], zoom_start=8)
        folium.Marker([enlem, boylam], popup="Hedef", icon=folium.Icon(color='black',icon_color='#FFFF00'),
                      draggable=False).add_to(map)

        if enlem != '' and boylam != '' and mesafe != '':

            for r in all_reports:
                sql1 = (float(enlem) - r.enlem) * (float(enlem) - r.enlem)
                sql2 = (float(boylam) - r.boylam) * (float(boylam) - r.boylam)
                q = (math.sqrt(sql1 + sql2)) * 1000
                if q <= float(mesafe):
                    query_reports.append(r)

            for q in query_reports:
                folium.Marker([q.enlem, q.boylam], popup=q.rapor_no,
                              draggable=False).add_to(map)

            map = map._repr_html_()

            context.update({
                'map': map
            })

        else:
            messages.warning(request, 'Tüm alanların doldurulması gereklidir!')
            return redirect('near_rapor')
    context.update({'query_reports': query_reports})

    return render(request, 'pages/near_reports.html', context)


@login_required(login_url="/giris-yap")
def maas(request):
    context = {}
    salary = Maas.objects.all()
    context.update({'salary': salary})
    form = MaasAddForm(data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    if 'salary_add' in request.POST:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, 'Maaş başarıyla eklendi!')
            return redirect('maas')
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('maas')

    return render(request, 'pages/salary.html', context)


@login_required(login_url="/giris-yap")
def delete_maas(request, id):
    salary = Maas.objects.get(id=id)
    salary.delete()
    messages.success(request, 'Maaş başarıyla silindi!')
    return redirect('maas')


@login_required(login_url="/giris-yap")
def update_maas(request, id):
    context = {}
    salary = Maas.objects.get(id=id)
    context.update({'salary': salary})
    form = MaasUpdateForm(instance=salary, data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    if 'salary_update' in request.POST:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, 'Maaş başarıyla güncellendi!')
            return redirect('update_maas', id)
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('update_maas', id)

    return render(request, 'pages/salary_update.html', context)


@login_required(login_url="/giris-yap")
def arac_kirasi(request):
    context = {}
    rent = AracKira.objects.all()
    context.update({'rent': rent})
    form = AracKirasiAddForm(data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    if 'rent_add' in request.POST:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, 'Araç kirası başarıyla eklendi!')
            return redirect('arac_kirasi')
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('arac_kirasi')

    return render(request, 'pages/car_rental.html', context)


@login_required(login_url="/giris-yap")
def delete_arac_kirasi(request, id):
    rent = AracKira.objects.get(id=id)
    rent.delete()
    messages.success(request, 'Araç kirası başarıyla silindi!')
    return redirect('arac_kirasi')


@login_required(login_url="/giris-yap")
def update_arac_kirasi(request, id):
    context = {}
    rent = AracKira.objects.get(id=id)
    context.update({'rent': rent})
    form = AracKiraUpdateForm(instance=rent, data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    if 'rent_update' in request.POST:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, 'Maaş başarıyla güncellendi!')
            return redirect('update_arac_kirasi', id)
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('update_arac_kirasi', id)

    return render(request, 'pages/carrental_update.html', context)


@login_required(login_url="/giris-yap")
def prim(request):
    context = {}
    prim = Prim.objects.all()
    context.update({'prim': prim})
    form = PrimAddForm(data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    count = 0

    if 'prim_add' in request.POST:
        rapor_no = request.POST.get('rapor_no', None)
        prim = request.POST.get('prim', None)

        if rapor_no != '' and prim != '':
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                data.save()
                messages.success(request, 'Prim başarıyla eklendi!')
                return redirect('prim')
            else:
                messages.warning(request, 'Bir hata meydana geldi!')
                return redirect('prim')
        else:
            messages.warning(request, 'Tüm alanların doldurulması gerekmektedir!')
            return redirect('prim')

    if 'prim_query' in request.POST:
        yil = request.POST.get('yil', None)
        ay = request.POST.get('ay', None)

        if yil != '' and ay != '':
            count = 1
            primler = Prim.objects.filter(yil=yil, ay=ay)
            print(primler)
            return redirect('prim')
        else:
            messages.warning(request, 'Yıl ve ay seçmeniz gerekmektedir.')
            return redirect('prim')

    return render(request, 'pages/prim.html', context)


@login_required(login_url="/giris-yap")
def delete_prim(request, id):
    prim = Prim.objects.get(id=id)
    prim.delete()
    messages.success(request, 'Pirim başarıyla silindi!')
    return redirect('prim')


@login_required(login_url="/giris-yap")
def update_prim(request, id):
    context = {}
    prim = Prim.objects.get(id=id)
    context.update({'prim': prim})
    form = PrimUpdateForm(instance=prim, data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    if 'prim_update' in request.POST:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, 'Prim başarıyla güncellendi!')
            return redirect('update_prim', id)
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('update_prim', id)

    return render(request, 'pages/prim_update.html', context)


def get_json_prim(request, *args, **kwargs):
    yil = kwargs.get('yil')
    ay = kwargs.get('ay')
    user = request.user

    primler = Prim.objects.filter(user=user, yil=yil, ay=ay)
    ucret = 0

    for p in primler:
        ucret += p.prim

    prim = ucret * 0.1

    return JsonResponse({'data': prim})


@login_required(login_url="/giris-yap")
def yapi_birim_maliyetleri(request):
    context = {}
    maliyetler = YapiMaliyetleri.objects.all()
    context.update({'maliyetler': maliyetler})
    form = YapiMaliyetAddForm(data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    if 'coast_add' in request.POST:
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Yapı birim maliyeti eklendi!')
            return redirect('yapi_birim_maliyetleri')
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('yapi_birim_maliyetleri')

    return render(request, 'pages/build_coast.html', context)


@login_required(login_url="/giris-yap")
def delete_yapi_birim_maliyeti(request, id):
    maliyet = YapiMaliyetleri.objects.get(id=id)
    maliyet.delete()
    messages.success(request, 'Yapı birim maliyeti başarıyla silindi!')
    return redirect('yapi_birim_maliyetleri')


@login_required(login_url="/giris-yap")
def update_yapi_birim_maliyeti(request, id):
    context = {}
    maliyet = YapiMaliyetleri.objects.get(id=id)
    context.update({'maliyet': maliyet})
    form = YapiMaliyetleriUpdateForm(instance=maliyet, data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    if 'coast_update' in request.POST:
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Yapı birim maliyetleri başarıyla güncellendi!')
            return redirect('update_yapi_birim_maliyeti', id)
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('update_yapi_birim_maliyeti', id)

    return render(request, 'pages/buildcoast_update.html', context)


@login_required(login_url="/giris-yap")
def imar_plani_onay_tarihleri(request):
    context = {}
    tarihler = ImarPlanOnaylari.objects.all()
    context.update({'tarihler': tarihler})
    form = ImarTarihiAddForm(data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    if 'date_add' in request.POST:
        if form.is_valid():
            form.save()
            messages.success(request, 'İmar planı onay tarihi başarıyla eklendi!')
            return redirect('imar_plani_onay_tarihleri')
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('imar_plani_onay_tarihleri')

    return render(request, 'pages/imar_plani.html', context)


@login_required(login_url="/giris-yap")
def delete_imarplani_onay_tarihi(request, id):
    tarih = ImarPlanOnaylari.objects.get(id=id)
    tarih.delete()
    messages.success(request, 'İmar planı onay tarihi başarıyla silindi!')
    return redirect('imar_plani_onay_tarihleri')


@login_required(login_url="/giris-yap")
def update_imar_plani_onay_tarihi(request, id):
    context = {}
    tarih = ImarPlanOnaylari.objects.get(id=id)
    context.update({'tarih': tarih})
    form = ImarTarihiUpdateForm(instance=tarih, data=request.POST or None, files=request.FILES or None)
    context.update({'form': form})

    if 'date_update' in request.POST:
        if form.is_valid():
            form.save()
            messages.success(request, 'İmar planı onay tarihi başarıyla güncellendi!')
            return redirect('update_imar_plani_onay_tarihi', id)
        else:
            messages.warning(request, 'Bir hata meydana geldi!')
            return redirect('update_imar_plani_onay_tarihi', id)

    return render(request, 'pages/imarplani_update.html', context)


def load_ilceler(request):
    city_id = request.GET.get('city_id')
    ilceler = County.objects.filter(city_id=city_id)
    return render(request, 'partials/dropdown_ilceler.html', {'ilceler': ilceler})


def load_mahalleler(request):
    county_id = request.GET.get('county_id')
    mahalleler = Neighbourhood.objects.filter(county_id=county_id)
    return render(request, 'partials/dropdown_mahalleler.html', {'mahalleler': mahalleler})
