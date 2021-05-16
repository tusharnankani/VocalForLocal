from django.http import HttpResponse
from django.shortcuts import render , redirect

# import your forms here

from .forms import *


def homepage(request):
  form = LoginForm()
  if request.method == 'POST' : 
    form = LoginForm(request.POST)
    if form.is_valid() : 
      data = form.cleaned_data
      print(data)

      if data['usertype'] == 'customer' : 
        print('redirect to customer dashboard')
        return redirect('/customer_dashboard')

      elif data['usertype'] == 'business':
        print('redirect to business dashboard')
        return redirect('/seller_dashboard')

    else : 
      print('ERROR')
      print(request.POST)
      
  return render(request, "accounts/index.html")

def customer_dashboard(request):
  return render(request,'accounts/customer-dashboard.html')

def seller_dashboard(request):
  return render(request,'accounts/seller-dashboard.html')

# def seller_register(request):
#   return HttpResponse("seller register from here")
#   #return render(request,'login.html')

