from datetime import datetime,timedelta
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from rest_framework.decorators import api_view
from .serializers import UserSerializer,Donor_detailsSerializer,Donorsorted_detailsSerializer,Request_detailsSerializers,BloodbankSerializer
from rest_framework import generics,viewsets
from .models import Donor_details,Request_details,Bloodbank
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView



class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DonordetailView(viewsets.ModelViewSet):
    queryset = Donor_details.objects.all()
    serializer_class = Donor_detailsSerializer

class BloodbankView(viewsets.ModelViewSet):
    queryset = Bloodbank.objects.all()
    serializer_class = BloodbankSerializer


class RequestList(APIView):
    def get(self, request, format=None):
        acceptor = Request_details.objects.all()
        serializer = Request_detailsSerializers(acceptor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Request_detailsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SortedView(APIView):
    def get(self, request, format=None):
        acceptor = Request_details.objects.all()
        serializer = Request_detailsSerializers(acceptor, many=True)
        return Response(serializer.data)
  
    def post(self,request):
        if "registration_id" in request.data:
            registration_id = request.data.get('registration_id')
            four_months_ago = 4

            user_location = Request_details.objects.filter(registration_id=registration_id).values_list('location',flat=True)[0]
            blood_group = Request_details.objects.filter(registration_id=registration_id).values_list('Bloodgroup',flat=True)[0]
            d =datetime.now()
            donor_sorted = Donor_details.objects.annotate(distance=Distance('location',user_location)).filter(Bloodgroup = blood_group,last_blood_given_on__gte=d-timedelta(days=112)).order_by('distance')[0:3]
            serializer = Donorsorted_detailsSerializer(donor_sorted, many=True)
            
            
            primary=Request_details()
            old_data =Request_details.objects.get(pk=registration_id)
            donor_sortedlist = serializer.data
            primary=Request_details(donor_details=donor_sortedlist,pk=registration_id,Bloodbank=old_data.Bloodbank,
            location =old_data.location,first_name=old_data.first_name,last_name=old_data.last_name,email=old_data.email,Bloodgroup=old_data.Bloodgroup,
            address=old_data.address,city=old_data.city,phone=old_data.phone)
            primary.pk = registration_id
            primary.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
            


        # {"registration_id":"67020B"}