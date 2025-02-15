"""
URL configuration for evss project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
from User_Homepage import views

urlpatterns = [
    path("", include("loginPage.urls")),
    #path('admin/', admin.site.urls),
    # path('homepage/',views.homepage,name="homepage"),
    # path('rent/',views.rent_page,name='rent_page'),
    # path('time/',views.time_page,name='time_page'),
    # path('rent_vehicle/<int:vehicle_id>/', views.rent_vehicle, name='rent_vehicle'),
    # #path('drop_vehicle/<int:vehicle_id>/', views.drop_vehicle, name='drop_vehicle'),
    # path('create_rental/', views.create_rental, name='create_rental'),
    path('admin/', admin.site.urls),
    path('auth/', include('eshareauth.urls')),
    path('auth/', include('User_Homepage.urls')),


]
