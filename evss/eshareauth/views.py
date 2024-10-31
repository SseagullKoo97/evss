import string
import random
import logging
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .forms import CustomerRegistrationForm, LoginForm
from .models import Customer, Wallet
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail, BadHeaderError
from .models import Manager, Operator


# Main index view, rendering the homepage
def index(request):
    return render(request, 'index.html')


# Customer login view, handling both GET and POST requests
@require_http_methods(['GET', 'POST'])
def customer_login(request):
    if request.method == 'GET':
        # Display the login form on GET request
        form = LoginForm()
        return render(request, 'customer_login.html', {'form': form})

    # Handle POST request for login
    form = LoginForm(request.POST)
    if form.is_valid():
        # Retrieve form data
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')

        # Check if customer exists with given email
        customer = Customer.objects.filter(email=email).first()
        if customer and check_password(password, customer.customer_password):
            print("Customer ID:", customer.customer_id)
            print(request.user.id)



            # Set session data for successful login
            request.session['customer_id'] = customer.customer_id
            request.session['is_customer_logged_in'] = True

            print(request.session['customer_id'])

            # If "remember me" is unchecked, set session expiry to end with browser session
            if not remember:
                request.session.set_expiry(0)

            messages.success(request, 'Customer login successful!')
            return redirect('eshareauth:index')
        else:
            messages.error(request, 'Wrong email or password.')
            return redirect(reverse('eshareauth:customer_login'))

    # Render login page with form errors if form is invalid
    return render(request, 'customer_login.html', {'form': form})


# Operator login view, handling both GET and POST requests
@require_http_methods(['GET', 'POST'])
def operator_login(request):
    if request.method == 'GET':
        # Display the login form on GET request
        form = LoginForm()
        return render(request, 'operator_login.html', {'form': form})

    # Handle POST request for login
    form = LoginForm(request.POST)
    if form.is_valid():
        # Retrieve form data
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')

        # Debug information for email and password
        print(f"Email: {email}, Password: {password}")

        # Check if operator exists with given email
        operator = Operator.objects.filter(operator_email=email).first()

        if operator:
            print("Operator found:", operator.operator_email)
            password_match = check_password(password, operator.operator_password)
            print("Password match:", password_match)

            if password_match:
                # Set session data for successful login
                request.session['operator_id'] = operator.id
                request.session['is_operator_logged_in'] = True

                # If "remember me" is unchecked, set session expiry to end with browser session
                if not remember:
                    request.session.set_expiry(0)

                messages.success(request, 'Operator login successful!')
                return redirect('eshareauth:index')
            else:
                print("Password did not match.")
        else:
            print("Operator not found.")

        messages.error(request, 'Wrong email or password.')
        return redirect(reverse('eshareauth:operator_login'))

    # Render login page with form errors if form is invalid
    return render(request, 'operator_login.html', {'form': form})


# Manager login view, handling both GET and POST requests
@require_http_methods(['GET', 'POST'])
def manager_login(request):
    if request.method == 'GET':
        # Display the login form on GET request
        form = LoginForm()
        return render(request, 'manager_login.html', {'form': form})

    # Handle POST request for login
    form = LoginForm(request.POST)
    if form.is_valid():
        # Retrieve form data
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')

        # Check if manager exists with given email
        manager = Manager.objects.filter(manager_email=email).first()
        if manager and check_password(password, manager.manager_password):
            # Set session data for successful login
            request.session['manager_id'] = manager.id
            request.session['is_manager_logged_in'] = True

            # If "remember me" is unchecked, set session expiry to end with browser session
            if not remember:
                request.session.set_expiry(0)

            messages.success(request, 'Manager login successful!')
            return redirect('eshareauth:index')
        else:
            messages.error(request, 'Wrong email or password.')
            return redirect(reverse('eshareauth:manager_login'))

    # Render login page with form errors if form is invalid
    return render(request, 'manager_login.html', {'form': form})


# Logout view to clear session and redirect to homepage
def esharelogout(request):
    request.session.flush()  # Clear session data
    messages.success(request, "You have been logged out.")
    return redirect('index')


# Customer registration view, handling both GET and POST requests
@require_http_methods(['GET', 'POST'])
def customer_register(request):
    if request.method == 'GET':
        # Display the registration form on GET request
        return render(request, 'customer_register.html')
    else:
        # Handle POST request for registration
        form = CustomerRegistrationForm(request.POST, request=request)
        if form.is_valid():
            # Retrieve form data
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            dob = form.cleaned_data.get('dob')
            deposit = form.cleaned_data.get('deposit')
            phone_number = form.cleaned_data.get('phone_number')

            # Hash password before saving it in the database
            hashed_password = make_password(password)

            # Create customer and associated wallet
            user = Customer.objects.create(
                email=email,
                customer_name=f"{first_name} {last_name}",
                customer_password=hashed_password,
                dateofbirth=dob,
                customer_number=phone_number
            )
            wallet = Wallet.objects.create(customer=user, balance=deposit)
            user.wallet = wallet
            user.save()

            messages.success(request, 'You have successfully registered!')
            return redirect(reverse('eshareauth:customer_login'))
        else:
            # Display form errors
            for field, errors in form.errors.items():
                print(f"Error in {field}: {errors}")
            messages.error(request, 'There was an error in the registration form.')
            return render(request, 'customer_register.html', {'form': form})


# View to send an email CAPTCHA (verification code) to the user's email address
logger = logging.getLogger(__name__)  # Set up logging

def send_email_captcha(request):
    email = request.GET.get('email')
    if not email:
        # Return error if email is missing
        return JsonResponse({"code": 400, "message": 'Email is required'})

    # Generate a random 4-digit CAPTCHA code
    captcha = "".join(random.sample(string.digits, 4))
    # Save CAPTCHA to the session
    request.session['email_captcha'] = captcha

    try:
        # Send the CAPTCHA to the user's email
        send_mail(
            "Registration verification code",
            message=f"Your registration verification code is: {captcha}",
            recipient_list=[email],
            from_email=None
        )
        return JsonResponse({"code": 200, "message": "CAPTCHA sent successfully"})

    except BadHeaderError:
        logger.error("Invalid header found.")
        return JsonResponse({"code": 500, "message": "Invalid header found."})
    except Exception as e:
        # Log specific error
        logger.error(f"Error sending email: {str(e)}")
        return JsonResponse({"code": 500, "message": f"An error occurred while sending the email: {str(e)}"})


# View to verify CAPTCHA entered by the user
@require_http_methods(["POST"])
def verify_captcha(request):
    user_input_captcha = request.POST.get('captcha')
    session_captcha = request.session.get('email_captcha')

    if user_input_captcha == session_captcha:
        # If CAPTCHA is correct, remove it from session
        del request.session['email_captcha']
        messages.success(request, "Captcha verified successfully.")
        return redirect("eshareauth:index")
    else:
        messages.error(request, "Verification code is not correct.")
        return redirect("eshareauth:customer_register")





