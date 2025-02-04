from django.urls import path
 
from .views import *

urlpatterns = [
 
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),  
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),  
] 
