# Generated by Django 4.1.4 on 2023-03-19 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert_info', '0009_alter_arackira_yil_alter_maas_yil'),
    ]

    operations = [
        migrations.CreateModel(
            name='YapiMaliyetleri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yapi_sinifi', models.CharField(max_length=10, null=True, verbose_name='Yapı Sınıfı')),
                ('birim_maliyet', models.FloatField(null=True, verbose_name='Birim Maliyet')),
            ],
            options={
                'verbose_name': 'Yapı Birim Maliyetleri',
                'verbose_name_plural': 'Yapı Birim Maliyetleri',
            },
        ),
    ]
