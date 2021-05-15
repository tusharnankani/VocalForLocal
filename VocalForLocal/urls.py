
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #registered/not-registered customer
    path('customer-dashboard/',views.customer_dashboard),   

    #registered seller
    path('seller-dashboard/',views.seller_dashboard),

    #not-registered seller 
    path('seller-register/',views.seller_register),

    path('',views.homepage),    
    
]
