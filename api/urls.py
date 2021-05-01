from django.urls import include, path
from rest_framework import routers
from .views import (UserViewSet, HospitalList, OxygenList, HospitalAvailableList,
                     OxygenFilterList, OxygenAvailableList,MedList,NoticeList)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('hospitals/',HospitalList.as_view(),name='hospitals'),
    path('hospitals-available/',HospitalAvailableList.as_view(),name='hospital_available'),
    path('oxygen/',OxygenList.as_view(),name='oxygen'),
    path('oxygen-available/',OxygenAvailableList.as_view(),name='oxygen_available'),
    path('oxygen/<filter_>/',OxygenFilterList.as_view(),name='oxygen_filter'),
    path('meds/',MedList.as_view(),name='med-list'),
    path('notice/',NoticeList.as_view(),name='notice-list')
]