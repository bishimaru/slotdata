# Generated by Django 3.2.5 on 2021-07-21 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_alter_slotdata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slotdata',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 21, 17, 26, 40, 652170), verbose_name='日付'),
        ),
    ]
