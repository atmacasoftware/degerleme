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
def mainpage(request):
    return render(request, 'pages/mainpage.html')


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
    counties = County.objects.all()
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
    context.update({'city': city,'county':county})
    neig = Neighbourhood.objects.all()
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