from django.urls import path
from . import views

urlpatterns = [
    path('denetim/', views.denetim, name='denetim'),
    path('yonet/', views.denetim, name='denetim'),]
