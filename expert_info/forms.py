from django import forms
from expert_info.models import *


class RaporEkleAddForm(forms.ModelForm):
    deger_tarihi = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = RaporEkle
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(RaporEkleAddForm, self).__init__(*args, **kwargs)
        self.fields['il'].queryset = Citys.objects.none()
        self.fields['ilce'].queryset = County.objects.none()
        self.fields['mahalle'].queryset = Neighbourhood.objects.none()

        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class RaporEkleUpdateForm(forms.ModelForm):
    class Meta:
        model = RaporEkle
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(RaporEkleUpdateForm, self).__init__(*args, **kwargs)
        self.fields['ilce'].queryset = County.objects.none()
        self.fields['mahalle'].queryset = Neighbourhood.objects.none()
        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['ilce'].queryset = County.objects.filter(country_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['ilce'].queryset = self.instance.il.county_set.order_by('name')

        if 'county' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['mahalle'].queryset = County.objects.filter(country_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['mahalle'].queryset = self.instance.ilce.neighbourhood_set.order_by('name')

        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

class MaasAddForm(forms.ModelForm):
    class Meta:
        model = Maas
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(MaasAddForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class MaasUpdateForm(forms.ModelForm):
    class Meta:
        model = Maas
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(MaasUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

class AracKirasiAddForm(forms.ModelForm):
    class Meta:
        model = AracKira
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(AracKirasiAddForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class AracKiraUpdateForm(forms.ModelForm):
    class Meta:
        model = AracKira
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(AracKiraUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class PrimAddForm(forms.ModelForm):
    class Meta:
        model = Prim
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(PrimAddForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class PrimUpdateForm(forms.ModelForm):
    class Meta:
        model = Prim
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(PrimUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class YapiMaliyetAddForm(forms.ModelForm):
    class Meta:
        model = YapiMaliyetleri
        fields = '__all__'
        exclude = ['created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(YapiMaliyetAddForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class YapiMaliyetleriUpdateForm(forms.ModelForm):
    class Meta:
        model = YapiMaliyetleri
        fields = '__all__'
        exclude = ['created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(YapiMaliyetleriUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class ImarTarihiAddForm(forms.ModelForm):
    tarih = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = ImarPlanOnaylari
        fields = '__all__'
        exclude = ['created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(ImarTarihiAddForm, self).__init__(*args, **kwargs)

        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['ilce'].queryset = County.objects.filter(country_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['ilce'].queryset = self.instance.il.county_set.order_by('name')

        if 'county' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['mahalle'].queryset = County.objects.filter(country_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['mahalle'].queryset = self.instance.ilce.neighbourhood_set.order_by('name')

        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class ImarTarihiUpdateForm(forms.ModelForm):
    tarih = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = ImarPlanOnaylari
        fields = '__all__'
        exclude = ['created_at', 'updated_at', 'is_exist']

    def __init__(self, *args, **kwargs):
        super(ImarTarihiUpdateForm, self).__init__(*args, **kwargs)
        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['ilce'].queryset = County.objects.filter(country_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['ilce'].queryset = self.instance.il.county_set.order_by('name')

        if 'county' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['mahalle'].queryset = County.objects.filter(country_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['mahalle'].queryset = self.instance.ilce.neighbourhood_set.order_by('name')

        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'