from django import forms
from .import models

class SellerRegisterForm(forms.Form):
  class Meta:
    model = models.Article
    fields = ['shop_name','shop_owner','address','phone','pincode','category']

class LoginForm(forms.Form):
  class Meta:
    model = models.Article
    fields = ['phonenumber','pincode']