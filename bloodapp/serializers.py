from rest_framework import serializers
from .models import Donor_details,Request_details,Bloodbank
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class Donor_detailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donor_details
        fields = '__all__'

class BloodbankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bloodbank
        fields = '__all__'

class Request_detailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Request_details
        fields = '__all__'


class Donorsorted_detailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donor_details
        fields = '__all__'

