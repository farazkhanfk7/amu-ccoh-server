from django.contrib import admin
from django.urls import path,include
from . import views
from .views import (HospitalView,HospitalDetailView,HospitalCreateView,
                    HospitalUpdateView,HospitalDeleteView)

urlpatterns = [
    path('',views.home,name="home"),
    path('hospitals/',HospitalView.as_view(),name="hospitals"),
    path('hospitals/new/',HospitalCreateView.as_view(),name='hospital-create'),
    path('hospitals/<int:pk>/edit/',HospitalUpdateView.as_view(),name="hospital-edit"),
    path('hospitals/<int:pk>/delete/',HospitalDeleteView.as_view(),name="hospital-delete"),
    path('hospitals/<int:pk>/',HospitalDetailView.as_view(),name="hospital-detail"),
]