# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20160803_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaicMortgageInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mortgage_id', models.CharField(max_length=255, verbose_name='\u5e8f\u53f7')),
                ('number', models.CharField(max_length=255, verbose_name='\u767b\u8bb0\u7f16\u53f7')),
                ('date', models.CharField(max_length=255, verbose_name='\u767b\u8bb0\u65e5\u671f')),
                ('reg_authority', models.CharField(max_length=255, verbose_name='\u767b\u8bb0\u673a\u5173')),
                ('Sclaims_Amount', models.CharField(max_length=255, verbose_name='\u88ab\u62c5\u4fdd\u503a\u6743\u6570\u989d')),
                ('status', models.CharField(max_length=255, verbose_name='\u72b6\u6001')),
                ('more', models.CharField(max_length=255, verbose_name='\u8be6\u60c5')),
            ],
        ),
        migrations.CreateModel(
            name='BaicRecordInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_id', models.CharField(max_length=255, verbose_name='\u4eba\u5458\u4fe1\u606f\u5e8f\u53f7')),
                ('person_name', models.CharField(max_length=255, verbose_name='\u4eba\u5458\u59d3\u540d')),
                ('person_post', models.CharField(max_length=255, verbose_name='\u4eba\u5458\u804c\u52a1')),
                ('Branch_id', models.CharField(max_length=255, verbose_name='\u5206\u652f\u673a\u6784\u5e8f\u53f7')),
                ('Branch_number', models.CharField(max_length=255, verbose_name='\u5206\u652f\u673a\u6ce8\u518c\u53f7')),
                ('Branch_name', models.CharField(max_length=255, verbose_name='\u5206\u652f\u673a\u6784\u540d\u79f0')),
                ('Branch_reg_auth', models.CharField(max_length=255, verbose_name='\u5206\u652f\u673a\u6784\u767b\u8bb0\u673a\u5173')),
                ('Liquidation_charge', models.CharField(max_length=255, verbose_name='\u6e05\u7b97\u7ec4\u8d1f\u8d23\u4eba')),
                ('Liquidation_Group', models.CharField(max_length=255, verbose_name='\u6e05\u7b97\u7ec4\u6210\u5458')),
            ],
        ),
        migrations.CreateModel(
            name='BaicStockIfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_id', models.CharField(max_length=255, verbose_name='\u5e8f\u53f7')),
                ('register_number', models.CharField(max_length=255, verbose_name='\u767b\u8bb0\u7f16\u53f7')),
                ('seller', models.CharField(max_length=255, verbose_name='\u51fa\u8d28\u4eba')),
                ('Cert_number', models.CharField(max_length=255, verbose_name='\u8bc1\u7167/\u8bc1\u4ef6\u53f7\u7801')),
                ('sale_count', models.CharField(max_length=255, verbose_name='\u51fa\u8d28\u80a1\u6743\u6570\u989d')),
                ('sale_owner', models.CharField(max_length=255, verbose_name='\u8d28\u6743\u4eba')),
                ('ID_number', models.CharField(max_length=255, verbose_name='\u8bc1\u7167/\u8bc1\u4ef6\u53f7\u7801')),
                ('reg_date', models.CharField(max_length=255, verbose_name='\u80a1\u6743\u51fa\u8d28\u8bbe\u7acb\u767b\u8bb0\u65e5\u671f')),
                ('status', models.CharField(max_length=255, verbose_name='\u72b6\u6001')),
                ('Change_status', models.CharField(max_length=255, verbose_name='\u53d8\u5316\u60c5\u51b5')),
            ],
        ),
    ]
