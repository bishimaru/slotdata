from django.urls import path
from . import views

app_name = 'list'

urlpatterns =[
    path('', views.index, name='index'),
    path('store_name/', views.StoreNameView.as_view(), name='store_name'),
]