from django.db import models
from address.models import *
from user_accounts.models import User


# Create your models here.

class RaporEkle(models.Model):
    ISINMA = (
        ('1', "MERKEZİ SİSTEM"),
        ('2', "KOMBİ"),
        ('3', "SOBA"),
        ('4', "YOK"),
        ('6', "DİĞER"),
    )

    ASANSOR = (
        ('1','VAR'),
        ('2','YOK'),
    )

    OTOPARK = (
        ('1', 'VAR'),
        ('2', 'YOK'),
    )

    GUVENLIK = (
        ('1', 'VAR'),
        ('2', 'YOK'),
    )

    YAPI_KALITE = (
        ('1', 'LÜKS'),
        ('2', 'İYİ'),
        ('3', 'ORTA'),
        ('4', 'DÜŞÜK'),
        ('5', 'YAPI YOK'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    rapor_no = models.CharField(max_length=255, verbose_name="Rapor Numarası", null=True, blank=False)
    il = models.ForeignKey(Citys, on_delete=models.CASCADE, verbose_name="İl")
    ilce = models.ForeignKey(County, on_delete=models.CASCADE, verbose_name="İlçe")
    mahalle = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, verbose_name="Mahalle")
    ada = models.BigIntegerField(verbose_name="Ada", null=True, blank=False)
    parsel = models.BigIntegerField(verbose_name="Parsel", null=True, blank=False)
    enlem = models.FloatField(verbose_name="Enlem", null=True, blank=False)
    boylam = models.FloatField(verbose_name="Boylam", null=True, blank=False)
    ana_tasinmaz_nitelik = models.CharField(max_length=500, verbose_name="Ana Taşınmaz Nitelik", null=True, blank=False)
    nitelik = models.CharField(max_length=500, verbose_name="Nitelik", null=True, blank=False)
    yuzolcum = models.FloatField(verbose_name="Yüzölçüm", null=True, blank=False)
    deger = models.FloatField(verbose_name="Değer", null=True, blank=False)
    kat = models.CharField(verbose_name="Kat", max_length=255, null=True, blank=True)
    oda_sayisi = models.CharField(verbose_name="Oda Sayısı", max_length=255, null=True, blank=True)
    isinma_sistemi = models.CharField(choices=ISINMA, max_length=255, verbose_name="Isınma Sistemi", null=True, blank=False)
    deger_tarihi = models.DateField(verbose_name="Değerleme Tarihi", null=True, blank=False)
    asansor = models.CharField(choices=ASANSOR, max_length=255, null=True, blank=False, verbose_name="Asansör")
    otopark = models.CharField(choices=OTOPARK, max_length=255,null=True, blank=False, verbose_name="Otopark")
    guvenlik = models.CharField(choices=GUVENLIK, max_length=255, null=True, blank=False, verbose_name="Güvenlik")
    yapi_kalitesi = models.CharField(choices=YAPI_KALITE, max_length=255, null=True, blank=False, verbose_name="Yapı Kalitesi")
    yapim_yili = models.PositiveBigIntegerField(verbose_name="Yapım Yılı", null=True, blank=True)
    dosya_konumu = models.CharField(max_length=500, verbose_name="Dosya Konumu", null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_exist = models.BooleanField(default=True, null=True, verbose_name="Mevcut mu?")

    class Meta:
        verbose_name = "Eklenen Raporlar"
        verbose_name_plural = "Eklenen Raporlar"

    def __str__(self):
        return f"{self.rapor_no}"


class Maas(models.Model):
    YIL = (
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
        ('2031', '2031'),
        ('2032', '2032'),
        ('2033', '2033'),
        ('2034', '2034'),
    )

    AY = (
        ('1','Ocak'),
        ('2','Şubat'),
        ('3','Mart'),
        ('4','Nisan'),
        ('5','Mayıs'),
        ('6','Haziran'),
        ('7','Temmuz'),
        ('8','Ağustos'),
        ('9','Eylül'),
        ('10','Ekim'),
        ('11','Kasım'),
        ('12','Aralık'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    yil = models.CharField(choices=YIL, max_length=50, verbose_name="Yıl", null=True, blank=False)
    ay = models.CharField(choices=AY, max_length=50, verbose_name="Ay", null=True, blank=False)
    maas = models.FloatField(verbose_name="Maaş", null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_exist = models.BooleanField(default=True, null=True, verbose_name="Mevcut mu?")

    class Meta:
        verbose_name = "Maaşlar"
        verbose_name_plural = "Maaşlar"

    def __str__(self):
        return f"{self.user}"


class AracKira(models.Model):
    YIL = (
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
        ('2031', '2031'),
        ('2032', '2032'),
        ('2033', '2033'),
        ('2034', '2034'),
    )

    AY = (
        ('1','Ocak'),
        ('2','Şubat'),
        ('3','Mart'),
        ('4','Nisan'),
        ('5','Mayıs'),
        ('6','Haziran'),
        ('7','Temmuz'),
        ('8','Ağustos'),
        ('9','Eylül'),
        ('10','Ekim'),
        ('11','Kasım'),
        ('12','Aralık'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    yil = models.CharField(choices=YIL, max_length=50, verbose_name="Yıl", null=True, blank=False)
    ay = models.CharField(choices=AY, max_length=50, verbose_name="Ay", null=True, blank=False)
    kira = models.FloatField(verbose_name="Araç Kirası", null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_exist = models.BooleanField(default=True, null=True, verbose_name="Mevcut mu?")

    class Meta:
        verbose_name = "Araç Kiraları"
        verbose_name_plural = "Araç Kiraları"

    def __str__(self):
        return f"{self.user}"

class Prim(models.Model):

    YIL = (
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
        ('2031', '2031'),
        ('2032', '2032'),
        ('2033', '2033'),
        ('2034', '2034'),
    )

    AY = (
        ('1','Ocak'),
        ('2','Şubat'),
        ('3','Mart'),
        ('4','Nisan'),
        ('5','Mayıs'),
        ('6','Haziran'),
        ('7','Temmuz'),
        ('8','Ağustos'),
        ('9','Eylül'),
        ('10','Ekim'),
        ('11','Kasım'),
        ('12','Aralık'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    rapor_no = models.CharField(max_length=500, null=True, blank=True, verbose_name="Rapor Numarası")
    yil = models.CharField(choices=YIL, max_length=50, verbose_name="Yıl", null=True, blank=False)
    ay = models.CharField(choices=AY, max_length=50, verbose_name="Ay", null=True, blank=False)
    prim = models.FloatField(verbose_name="Rapor Ücreti", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_exist = models.BooleanField(default=True, null=True, verbose_name="Mevcut mu?")

    class Meta:
        verbose_name = "Primler"
        verbose_name_plural = "Primler"

    def __str__(self):
        return f"{self.user}"


class YapiMaliyetleri(models.Model):
    yapi_sinifi = models.CharField(max_length=10, verbose_name="Yapı Sınıfı", null=True, blank=False)
    birim_maliyet = models.FloatField(verbose_name="Birim Maliyet", null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_exist = models.BooleanField(default=True, null=True, verbose_name="Mevcut mu?")

    class Meta:
        verbose_name = "Yapı Birim Maliyetleri"
        verbose_name_plural = "Yapı Birim Maliyetleri"

    def __str__(self):
        return f"{self.yapi_sinifi}"

class ImarPlanOnaylari(models.Model):
    il = models.ForeignKey(Citys, on_delete=models.CASCADE, verbose_name="İl")
    ilce = models.ForeignKey(County, on_delete=models.CASCADE, verbose_name="İlçe")
    mahalle = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, verbose_name="Mahalle")
    ada = models.BigIntegerField(verbose_name="Ada", null=True, blank=False)
    parsel = models.BigIntegerField(verbose_name="Parsel", null=True, blank=False)
    tarih = models.DateField(verbose_name="Onay Tarihi", null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_exist = models.BooleanField(default=True, null=True, verbose_name="Mevcut mu?")

    class Meta:
        verbose_name = "İmar Planı Onay Tarihleri"
        verbose_name_plural = "İmar Planı Onay Tarihleri"
