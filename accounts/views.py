from django.http import HttpResponse
from django.shortcuts import render 

def homepage(request):
  return render(request, "accounts/index.html")
  #return render(request,'homepage.html')

# def customer_dashboard(request):
#   #return HttpResponse("customer dashboard template")
#   return render(request,'customer-dashboard.html')

# def seller_dashboard(request):
#   return HttpResponse("seller dashboard template")
#   #return render(request,'login.html')

# def seller_register(request):
#   return HttpResponse("seller register from here")
#   #return render(request,'login.html')

