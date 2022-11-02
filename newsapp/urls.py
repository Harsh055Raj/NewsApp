from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news_api.urls')),
    path('', TemplateView.as_view(template_name="home.html")),
    path('accounts/', include('allauth.urls')),
    #path('logout/',LogoutView.as_view(), name="logout"),
    #path('logout', LogoutView.as_view()),
    #path('logout/', views.logoutpage, name="logout")
    
]
