from django.urls import path
from . import views

# Namespace for the app's URLs to differentiate from other apps
app_name = 'eshareauth'

# Define URL patterns for the 'eshareauth' app
urlpatterns = [
    # Main index page, renders the homepage of the application
    path('', views.index, name='index'),

    # Login page for customers
    path('login/customer', views.customer_login, name='customer_login'),

    # Login page for operators
    path('login/operator', views.operator_login, name='operator_login'),

    # Login page for managers
    path('login/manager', views.manager_login, name='manager_login'),

    # Customer registration page, allowing new customers to register
    path('register/customer', views.customer_register, name='customer_register'),

    # Logout page, used to log out users from the application
    path('logout', views.esharelogout, name='logout'),

    # CAPTCHA email sending endpoint, used to send verification code to the user's email
    path('send_email_captcha/', views.send_email_captcha, name='send_email_captcha'),  # This is for sending the CAPTCHA

    # CAPTCHA verification endpoint, used to verify the entered CAPTCHA code
    path('verify_captcha/', views.verify_captcha, name='verify_captcha')  # This is for verifying the CAPTCHA
]

