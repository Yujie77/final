from django.urls import path

from . import views

urlpatterns = [
    path('add/',views.add_squirrel),
    path('<str:squirrel_id>/',views.edit_squirrel),
    path('', views.all_squirrels),
    #path('<char:squirrel_uniqueid>/',views.squirrel_details),#design a function squirrel_details in views.py
    #path('<char:squirrel_latitude>/',views.squirrel_details)
    #path('<char:squirrel_longitude>/',views.squirrel_details)
    #path('<char:squirrel_shift>/',views.squirrel_details)
    #path('<char:squirrel_Date>/',views.squirrel_details)
    #path('<char:squirrel_Age>/',views.squirrel_details)
    #path('<char:squirrel_furcolor>/',views.squirrel_details)
    #path('<char:squirrel_location>/',views.squirrel_details)
    #path('<char:squirrel_specificlocation>/',views.squirrel_details)
    #path('<char:squirrel_running>/',views.squirrel_details)
    #path('<char:squirrel_chasing>/',views.squirrel_details)
    #path('<char:squirrel_climbing>/',views.squirrel_details)
    #path('<char:squirrel_eating>/',views.squirrel_details)
    #path('<char:squirrel_foraging>/',views.squirrel_details)
    #path('<char:squirrel_otheractivities>/',views.squirrel_details)
    #path('<char:squirrel_kuks>/',views.squirrel_details)
    #path('<char:squirrel_quaas>/',views.squirrel_details)
    #path('<char:squirrel_moans>/',views.squirrel_details)
    #path('<char:squirrel_tailflags>/',views.squirrel_details)
    #path('<char:squirrel_tailtwitches>/',views.squirrel_details)
    #path('<char:squirrel_approaches>/',views.squirrel_details)
    #path('<char:squirrel_indifferent>/',views.squirrel_details)
    #path('<char:squirrel_runsfrom>/',views.squirrel_details)
]

