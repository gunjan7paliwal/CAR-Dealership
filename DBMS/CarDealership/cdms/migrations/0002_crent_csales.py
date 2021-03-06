# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crent',
            fields=[
                ('rentid', models.AutoField(primary_key=True, serialize=False)),
                ('custid', models.IntegerField(blank=True, null=True)),
                ('dealerid', models.IntegerField(blank=True, null=True)),
                ('vehid', models.IntegerField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=10, null=True)),
                ('rentdate', models.DateField(blank=True, null=True)),
                ('returndate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'crent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Csales',
            fields=[
                ('vehid', models.IntegerField(blank=True, null=True)),
                ('custid', models.IntegerField(blank=True, null=True)),
                ('dealerid', models.IntegerField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('saledate', models.DateField(blank=True, null=True)),
                ('paidby', models.CharField(blank=True, max_length=20, null=True)),
                ('saleid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'csales',
                'managed': False,
            },
        ),
    ]
