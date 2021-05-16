from django import forms
from .import models

# class SellerRegisterForm(forms.Form):
#   class Meta:
#     model = models.Article
#     fields = ['shop_name','shop_owner','address','phone','pincode','category']

class LoginForm(forms.Form):
  number = forms.CharField(max_length = 10, label = 'number')
  otp = forms.CharField(max_length = 4, label = 'otp')
  usertype = forms.CharField(max_length = 20, label = 'usertype')