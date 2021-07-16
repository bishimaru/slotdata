from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import SlotData
import datetime

class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()


class StoreNameView(ListView):
    model = SlotData
    template_name = 'store_name.html'

    # SlotDataの全データを取得するメソッドを定義
    def queryset(self):
        return SlotData.objects.all().distinct().values("store_name")
    

class DateView(ListView):
    model = SlotData
    template_name ='date.html'
    
    
    def queryset(self):
        name = self.request.GET.get('sn')
        dates = SlotData.objects.filter(store_name=name)
        return dates
    
class DetailView(ListView):
    model = SlotData
    template_name ='detail.html'
    
    
    def queryset(self):
        name = self.request.GET.get('sn')
        day = self.request.GET.get('date')
        # d = (str)(date)
        # dte = datetime.datetime.strptime(d, '%Y%m%d')
        dates = SlotData.objects.filter(store_name=name, date=day)
        return dates
    
  
    
    