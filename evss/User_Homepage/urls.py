
from django.urls import path, include
from django.urls import include, path
from . import views

app_name = 'User_Homepage'
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('rent/',views.rent_page,name='rent_page'),
    path('time/',views.time_page,name='time_page'),
    path('rent_vehicle/<int:vehicle_id>/', views.rent_vehicle, name='rent_vehicle'),
    #path('drop_vehicle/<int:vehicle_id>/', views.drop_vehicle, name='drop_vehicle'),
    path('create_rental/', views.create_rental, name='create_rental'),

]
