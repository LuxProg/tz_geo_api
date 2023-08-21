from django.urls import path
from . import views

# /maps/
urlpatterns = [
    path('', views.maps_home, name='maps_home'),
    path('main', views.main_map, name='main_map'),
]
