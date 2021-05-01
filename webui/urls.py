from django.contrib import admin
from django.urls import path,include
from . import views
from .views import (HospitalView,HospitalDetailView,HospitalCreateView,
                    HospitalUpdateView,HospitalDeleteView,OxygenView,
                    OxygenDetailView,OxygenCreateView,OxygenUpdateView,
                    OxygenDeleteView,MedsView,MedsDetailView,MedsCreateView,
                    MedsUpdateView,MedsDeleteView,NoticeView,NoticeCreateView,
                    NoticeUpdateView,NoticeDeleteView)

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
    path('meds/',MedsView.as_view(),name="meds"),
    path('meds/new/',MedsCreateView.as_view(),name='meds-create'),
    path('meds/<int:pk>/',MedsDetailView.as_view(),name="meds-detail"),
    path('meds/<int:pk>/edit/',MedsUpdateView.as_view(),name="meds-edit"),
    path('meds/<int:pk>/delete/',MedsDeleteView.as_view(),name="meds-delete"),
    path('notice/',NoticeView.as_view(),name="notice"),
    path('notice/new/',NoticeCreateView.as_view(),name='notice-create'),
    path('notice/<int:pk>/edit/',NoticeUpdateView.as_view(),name="notice-edit"),
    path('notice/<int:pk>/delete/',NoticeDeleteView.as_view(),name="notice-delete"),
]