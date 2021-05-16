from django.http import HttpResponse
from django.shortcuts import render , redirect

# import your forms here

from .forms import *
from .models import *

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
        if Seller.objects.filter(phone = data['number']).exists():
          seller = Seller.objects.get(phone = data['number'])
          print('redirect to business dashboard/shop name')
          return redirect("/seller_dashboard/{}".format(seller.shop_name))
        else:
          return redirect("/seller_register")


    else : 
      print('ERROR')
      print(request.POST)
      
  return render(request, "accounts/index.html")

def customer_dashboard(request):
  return render(request,'accounts/customer-dashboard.html')


def seller_dashboard(request,name):
  seller = Seller.objects.get(shop_name=name)
  print(seller)
  context = {"name":seller.shop_name,"owner":seller.shop_owner,"address":seller.address,"time":seller.time,"phone":seller.phone,"pincode":seller.pincode,"category":seller.category}
  return render(request,"accounts/seller-dashboard.html",context)

def seller_register(request):  
  if request.method == 'POST':    
    data = request.POST

    seller = Seller(shop_name = data['shopname'],shop_owner = data['owner'],address = data['address'],time = data['timings'],phone = data['contact'],pincode = data['pincode'],category = data['category'])
    seller.save()
    
    print(seller)
    return redirect('/seller_dashboard/{}'.format(seller.shop_name))
  return render(request,'accounts/seller-register.html')
