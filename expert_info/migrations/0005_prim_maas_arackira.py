# Generated by Django 4.1.4 on 2023-03-18 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expert_info', '0004_raporekle_deger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rapor_no', models.CharField(max_length=500, null=True, verbose_name='Rapor Numarası')),
                ('yil', models.CharField(choices=[('1', '2023'), ('2', '2024'), ('3', '2025'), ('4', '2026'), ('5', '2027'), ('6', '2028'), ('7', '2029'), ('8', '2030'), ('9', '2031'), ('10', '2032'), ('11', '2033'), ('12', '2034')], max_length=50, null=True, verbose_name='Yıl')),
                ('ay', models.CharField(choices=[('1', 'Ocak'), ('2', 'Şubat'), ('3', 'Mart'), ('4', 'Nisan'), ('5', 'Mayıs'), ('6', 'Haziran'), ('7', 'Temmuz'), ('8', 'Ağustos'), ('9', 'Eylül'), ('10', 'Ekim'), ('11', 'Kasım'), ('12', 'Aralık')], max_length=50, null=True, verbose_name='Ay')),
                ('kira', models.FloatField(null=True, verbose_name='Araç Kirası')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_exist', models.BooleanField(default=True, null=True, verbose_name='Mevcut mu?')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Primler',
                'verbose_name_plural': 'Primler',
            },
        ),
        migrations.CreateModel(
            name='Maas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yil', models.CharField(choices=[('1', '2023'), ('2', '2024'), ('3', '2025'), ('4', '2026'), ('5', '2027'), ('6', '2028'), ('7', '2029'), ('8', '2030'), ('9', '2031'), ('10', '2032'), ('11', '2033'), ('12', '2034')], max_length=50, null=True, verbose_name='Yıl')),
                ('ay', models.CharField(choices=[('1', 'Ocak'), ('2', 'Şubat'), ('3', 'Mart'), ('4', 'Nisan'), ('5', 'Mayıs'), ('6', 'Haziran'), ('7', 'Temmuz'), ('8', 'Ağustos'), ('9', 'Eylül'), ('10', 'Ekim'), ('11', 'Kasım'), ('12', 'Aralık')], max_length=50, null=True, verbose_name='Ay')),
                ('maas', models.FloatField(null=True, verbose_name='Maaş')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_exist', models.BooleanField(default=True, null=True, verbose_name='Mevcut mu?')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Maaşlar',
                'verbose_name_plural': 'Maaşlar',
            },
        ),
        migrations.CreateModel(
            name='AracKira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yil', models.CharField(choices=[('1', '2023'), ('2', '2024'), ('3', '2025'), ('4', '2026'), ('5', '2027'), ('6', '2028'), ('7', '2029'), ('8', '2030'), ('9', '2031'), ('10', '2032'), ('11', '2033'), ('12', '2034')], max_length=50, null=True, verbose_name='Yıl')),
                ('ay', models.CharField(choices=[('1', 'Ocak'), ('2', 'Şubat'), ('3', 'Mart'), ('4', 'Nisan'), ('5', 'Mayıs'), ('6', 'Haziran'), ('7', 'Temmuz'), ('8', 'Ağustos'), ('9', 'Eylül'), ('10', 'Ekim'), ('11', 'Kasım'), ('12', 'Aralık')], max_length=50, null=True, verbose_name='Ay')),
                ('kira', models.FloatField(null=True, verbose_name='Araç Kirası')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_exist', models.BooleanField(default=True, null=True, verbose_name='Mevcut mu?')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Araç Kiraları',
                'verbose_name_plural': 'Araç Kiraları',
            },
        ),
    ]
