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
  sellers = Seller.objects.all()
  if request.method == 'POST' : 
    pin = request.POST['pincode']
    tag = request.POST['tag']
    tag = Tag.objects.get(name = tag)
    print(pin, tag)
    sellers = tag.seller_set.all()
    dct = {}
    sorted_sellers = []
    for i in range(0, len(sellers)) : 
      dct[i] = abs(int(sellers[i].pincode) - int(pin))
    values = sorted(dct.values())
    for i in values : 
      for key, value in dct.items() : 
        if value == i :
          sorted_sellers.append(i) 
    print(sorted_sellers)
    context = {'sellers' : sorted_sellers, 'sellers-range' : len(sorted_sellers)}
  context = {'sellers' : sellers, 'sellers-range' : len(sellers)}
  return render(request,'accounts/customer-dashboard.html', context)


def seller_dashboard(request,name):
  seller = Seller.objects.get(shop_name=name)
  print(seller)
  if request.method == 'POST' : 
    data = request.POST
    print(data)
    if Tag.objects.filter(name = request.POST['tag']).exists() : 
      tag = Tag.objects.get(name = request.POST['tag'])
    else : 
      tag = Tag(name = request.POST['tag'])
      tag.save()
    if tag in seller.tags.all() : 
      pass
    else : 
      seller.tags.add(tag)
  tags = seller.tags.all() 
  context = {"name":seller.shop_name,"owner":seller.shop_owner,"address":seller.address,"time":seller.time,"phone":seller.phone,"pincode":seller.pincode,"category":seller.category, 'tags' : tags}
  return render(request,"accounts/seller-dashboard.html",context)

# @login_required(login_url='seller_register/')
def seller_register(request):  
  if request.method == 'POST':    
    data = request.POST

    seller = Seller(shop_name = data['shopname'],shop_owner = data['owner'],address = data['address'],time = data['timings'],phone = data['contact'],pincode = data['pincode'],category = data['category'])
    seller.save()
    
    print(seller)
    return redirect('/seller_dashboard/{}'.format(seller.shop_name))
  return render(request,'accounts/seller-register.html')


def logout_view(request):
  if request.method == 'POST':
    logout(request)
    return redirect('/')