# Generated by Django 3.2.5 on 2021-07-21 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0009_auto_20210721_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slotdata',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 21, 18, 3, 17, 777364), verbose_name='日付'),
        ),
    ]
