from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view),
]
