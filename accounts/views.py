from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def login_view(request):
  return HttpResponse("login from here")
  #return render(request,'login.html')

def signup_view(request):
  return HttpResponse("signup from here")
  #return render(request,'signup.html')
