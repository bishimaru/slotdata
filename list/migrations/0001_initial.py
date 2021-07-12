# Generated by Django 3.2.5 on 2021-07-11 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlotData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100, verbose_name='店舗名')),
                ('name', models.CharField(max_length=100, verbose_name='機種名')),
                ('number', models.IntegerField(verbose_name='台番号')),
                ('date', models.DateField(default=datetime.datetime(2021, 7, 11, 21, 21, 16, 650671), verbose_name='日付')),
                ('bigbonus', models.IntegerField(verbose_name='BB')),
                ('regularbonus', models.IntegerField(verbose_name='RB')),
                ('count', models.IntegerField(verbose_name='総回転数')),
                ('payout', models.IntegerField(verbose_name='差枚数')),
                ('memo', models.CharField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name': 'データ一覧',
                'verbose_name_plural': 'データ一覧',
                'db_table': 'data',
            },
        ),
    ]
