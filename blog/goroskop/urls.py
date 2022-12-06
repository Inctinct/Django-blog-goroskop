from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.goroskop,name='goroskop'),
    path('kozerog/',views.kozerog,name='kozerog'),
    path('vodolei/',views.vodolei,name='vodolei'),
    path('ribi/',views.ribi,name='ribi'),
    path('oven/',views.oven,name='oven'),
    path('telec/',views.telec,name='telec'),
    path('bliznici/',views.bliznici,name='bliznici'),
    path('rak/',views.rak,name='rak'),
    path('lev/',views.lev,name='lev'),
    path('deva/',views.deva,name='deva'),
    path('vesi/',views.vesi,name='vesi'),
    path('skorpion/',views.skorpion,name='skorpion'),
    path('strelec/',views.strelec,name='strelec'),
    path('create_goros',views.create_goros, name='create_goros')
]

