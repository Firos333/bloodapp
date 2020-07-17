from django.urls import path
from.import views
from rest_framework import routers
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin


router = routers.SimpleRouter()
router.register(r'users',views.UserView,'user')
router.register(r'api/donor',views.DonordetailView,'donordetail')
router.register(r'api/bloodbank',views.BloodbankView,'bloodbank')
# router.register(r'api/acceptor/', views.AccepterList.as_view(),'acceptors'),

urlpatterns = [
    url(r'api/request/', views.RequestList.as_view()),
    path('api/sorted/',views.SortedView.as_view()),
]

urlpatterns += router.urls

