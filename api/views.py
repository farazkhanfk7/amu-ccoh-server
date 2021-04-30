from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import Hospital, OxygenSupplier
from .serializers import UserSerializer, HospitalSerializer, OxygenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from django.db.models.query_utils import Q

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]


@permission_classes((permissions.AllowAny,)) # This decorator to be used with APIView
class HospitalList(APIView):
    """
    List of all Available Hospitals
    """

    def get(self, request, format=None):
        hospital = Hospital.objects.all().order_by('-last_updated')
        serializer = HospitalSerializer(hospital, many=True)
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,)) # This decorator to be used with APIView
class HospitalAvailableList(APIView):
    """
    List of all Available Hospitals
    """

    def get_objects(self):
        try:
            hospital = Hospital.objects.filter(availablity='Yes').order_by('-last_updated')
            return hospital
        except Hospital.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        hospital = self.get_objects()
        serializer = HospitalSerializer(hospital, many=True)
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,)) # This decorator to be used with APIView
class OxygenList(APIView):
    """
    List of all OxygenSuppliers
    """

    def get_objects(self):
        try:
            oxygen = OxygenSupplier.objects.filter(availablity='Yes').order_by('-last_updated')
            return oxygen
        except OxygenSupplier.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        oxygen = self.get_objects()
        serializer = OxygenSerializer(oxygen, many=True)
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,)) # This decorator to be used with APIView
class OxygenAvailableList(APIView):
    """
    List of all Available OxygenSuppliers
    """

    def get(self, request, format=None):
        oxygen = OxygenSupplier.objects.all().order_by('-last_updated')
        serializer = OxygenSerializer(oxygen, many=True)
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,)) # This decorator to be used with APIView
class OxygenFilterList(APIView):
    """
    List of all Filtered OxygenSuppliers
    """
    def get_objects(self,filter_):
        try:
            if filter_ == 'buy':
                oxygen = (OxygenSupplier.objects.filter(Q(type_is='Seller') | Q(type_is='Both'))
                          .filter(availablity='Yes').order_by('-last_updated'))
                return oxygen
            elif filter_ == 'fill':
                oxygen = (OxygenSupplier.objects.filter(Q(type_is='Filling') | Q(type_is='Both'))
                          .filter(availablity='Yes').order_by('-last_updated'))
                return oxygen
        except OxygenSupplier.DoesNotExist:
            raise Http404

    def get(self, request, filter_, format=None):
        oxygen = self.get_objects(filter_)
        serializer = OxygenSerializer(oxygen, many=True)
        return Response(serializer.data)
