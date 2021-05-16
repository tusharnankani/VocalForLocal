from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('customer_dashboard', views.customer_dashboard, name = 'customer_dashboard'),
    path('seller_dashboard', views.seller_dashboard, name = 'seller_dashboard'),
]

    # parindas 

    
    # #registered/not-registered customer
    # path('customer-dashboard/',views.customer_dashboard),   

    # #registered seller
    # path('seller-dashboard/',views.seller_dashboard),

    # #not-registered seller 
    # path('seller-register/',views.seller_register),

    # path('',views.homepage),    
    

