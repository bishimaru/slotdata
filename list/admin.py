from django.contrib import admin
from .models import SlotData

class SlotDataAdmin(admin.ModelAdmin):
        
        list_display=('store_name', 'name','number', 'date', 'payout', 'memo')
admin.site.register(SlotData)
