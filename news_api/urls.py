from unicodedata import name
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logoutpage, name="logout"),
    path('login', views.login, name = "login"),
    path('index', views.index, name="index"),
    path('mail_letter/', views.mail_letter, name='mail-letter'),
    path('contact/', views.contact, name = "contact")
   #path('register', views.register, name="register"),
    #path('success', views.success, name="success"),

]