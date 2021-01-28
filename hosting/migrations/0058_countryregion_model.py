# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-22 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0057_add_simple_genders'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='country')),
                ('iso_code', models.CharField(max_length=4, verbose_name='ISO code')),
                ('latin_code', models.CharField(max_length=70, verbose_name='Normative code in latin letters')),
                ('latin_name', models.CharField(blank=True, max_length=70, verbose_name='Full name in latin letters')),
                ('local_code', models.CharField(blank=True, max_length=70, verbose_name='Normative code in local language')),
                ('local_name', models.CharField(blank=True, max_length=70, verbose_name='Full name in local language')),
                ('esperanto_name', models.CharField(blank=True, max_length=70, verbose_name='Name in Esperanto')),
            ],
            options={
                'verbose_name': 'subregion',
                'verbose_name_plural': 'subregions',
            },
        ),
        migrations.AlterUniqueTogether(
            name='countryregion',
            unique_together=set([('country', 'iso_code')]),
        ),
        migrations.AddIndex(
            model_name='countryregion',
            index=models.Index(fields=['country', 'iso_code', 'id'], name='countryregion_isocode_pk_idx'),
        ),
    ]