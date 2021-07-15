from django.db import models
from datetime import datetime


class SlotData(models.Model):
    class Meta:
        db_table = 'data'
        verbose_name ="スロットデータ"
        verbose_name_plural = 'スロットデータ'

    store_name = models.CharField(max_length=100, verbose_name='店舗名')
    name = models.CharField(max_length=100, verbose_name='機種名')
    number = models.IntegerField(verbose_name='台番号')
    date = models.DateField(verbose_name='日付', default=datetime.now())
    bigbonus = models.IntegerField(verbose_name='BB')
    regularbonus = models.IntegerField(verbose_name='RB')
    count =models.IntegerField(verbose_name='総回転数')
    payout = models.IntegerField(verbose_name='差枚数')
    memo = models.CharField(max_length=50, verbose_name='メモ', blank=True, null=True)

    def __str__(self):
       return self.name
