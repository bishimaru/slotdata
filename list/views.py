from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import SlotData

class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()


class StoreNameView(ListView):
    model = SlotData
    template_name = 'store_name.html'

    # SlotDataの全データを取得するメソッドを定義
    def queryset(self):
        return SlotData.objects.all()

