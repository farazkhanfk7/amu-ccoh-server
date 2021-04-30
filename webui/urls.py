from django.contrib import admin
from django.urls import path,include
from . import views
from .views import (HospitalView,HospitalDetailView,HospitalCreateView,
                    HospitalUpdateView,HospitalDeleteView,OxygenView,
                    OxygenDetailView,OxygenCreateView,OxygenUpdateView,
                    OxygenDeleteView)

urlpatterns = [
    path('',views.home,name="home"),
    path('hospitals/',HospitalView.as_view(),name="hospitals"),
    path('hospitals/new/',HospitalCreateView.as_view(),name='hospital-create'),
    path('hospitals/<int:pk>/edit/',HospitalUpdateView.as_view(),name="hospital-edit"),
    path('hospitals/<int:pk>/delete/',HospitalDeleteView.as_view(),name="hospital-delete"),
    path('hospitals/<int:pk>/',HospitalDetailView.as_view(),name="hospital-detail"),
    path('oxygen/',OxygenView.as_view(),name="oxygen"),
    path('oxygen/new/',OxygenCreateView.as_view(),name='oxygen-create'),
    path('oxygen/<int:pk>/',OxygenDetailView.as_view(),name="oxygen-detail"),
    path('oxygen/<int:pk>/edit/',OxygenUpdateView.as_view(),name="oxygen-edit"),
    path('oxygen/<int:pk>/delete/',OxygenDeleteView.as_view(),name="oxygen-delete"),
]