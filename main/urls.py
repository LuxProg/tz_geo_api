from django.urls import path
from . import views

# /main/
urlpatterns = [
    path('', views.index),
    path('about/', views.about)
]
