from django.contrib.auth.models import User
from .models import Hospital, OxygenSupplier, Med, Notice
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    staff_of = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = ['url', 'username', 'email','staff_of']


class HospitalSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    last_updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Hospital
        fields = ['name','address','contact','other_contact','availablity','tags','remarks','created_on','last_updated']


class OxygenSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    last_updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = OxygenSupplier
        fields = ['name','address','contact','other_contact','type_is','availablity','remarks','created_on','last_updated']


class MedSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    last_updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Med
        fields = ['name','address','contact','other_contact','availablity','tags','remarks','created_on','last_updated']


class NoticeSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    last_updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Notice
        fields = ['title','remarks','link','created_on','last_updated']