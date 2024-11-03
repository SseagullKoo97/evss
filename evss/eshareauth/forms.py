from django import forms
from django.contrib.auth import get_user_model
from .models import Customer

# Retrieve the custom user model, if defined, or Django's default User model
User = get_user_model()


# Customer registration form for new users
class CustomerRegistrationForm(forms.Form):

    # First name field with max and min length validations, along with custom error messages
    first_name = forms.CharField(
        max_length=20,
        min_length=2,
        required=True,
        error_messages={
            'required': 'Please enter your first name.',
            "max_length": "First name must be between 2 and 20 characters.",
            "min_length": "First name must be between 2 and 20 characters."
        }
    )

    # Last name field with max and min length validations, and custom error messages
    last_name = forms.CharField(
        max_length=20,
        min_length=2,
        required=True,
        error_messages={
            'required': 'Please enter your last name.',
            "max_length": "Last name must be between 2 and 20 characters.",
            "min_length": "Last name must be between 2 and 20 characters."
        }
    )

    # Email field with custom error messages for required and invalid input
    email = forms.EmailField(
        error_messages={
            'required': 'Please enter your email address.',
            'invalid': 'Please enter a valid email address.'
        }
    )

    # CAPTCHA field to verify the user's input; requires exactly 4 digits
    captcha = forms.CharField(max_length=4, min_length=4)

    # Password field with minimum length validation
    password = forms.CharField(max_length=20, min_length=6)

    # Confirm password field with min length validation and custom error message
    confirm_password = forms.CharField(
        max_length=20,
        min_length=6,
        error_messages={
            'required': 'Please confirm your password.',
            'min_length': 'Password must be at least 6 characters.'
        }
    )

    # Phone number field, optional, allows only digits up to 15 characters
    phone_number = forms.CharField(max_length=15, required=False)

    # Date of birth field with a specific input format and custom error message
    dob = forms.DateField(
        input_formats=['%d/%m/%Y'],
        required=False,
        error_messages={'invalid': 'Enter a valid date in DD/MM/YYYY format.'}
    )

    # Deposit selection field with choices of 500 or 1000, required
    deposit = forms.ChoiceField(
        choices=[(500, '£500'), (1000, '£1000')],
        required=True
    )

    # Custom validation to check if the email is unique
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check for existing email in the database
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

    # Validation for the phone number to ensure it only contains digits
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Check if the phone number contains only digits, if provided
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone_number

    # Custom __init__ method to store the request object, allowing access to the session
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extract request from kwargs
        super(CustomerRegistrationForm, self).__init__(*args, **kwargs)

    # Custom validation for CAPTCHA to check it matches the session-stored CAPTCHA
    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        session_captcha = self.request.session.get('email_captcha')
        # Compare user input CAPTCHA with session-stored CAPTCHA
        if captcha != session_captcha:
            raise forms.ValidationError('Verification code is incorrect.')
        return captcha

    # Clean method to ensure the password and confirm_password fields match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        # Raise an error if passwords do not match
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")


# Login form for general user authentication
class LoginForm(forms.Form):
    # Email field with error messages for required and invalid input
    email = forms.EmailField(
        error_messages={
            'required': 'Please enter your email address.',
            'invalid': 'Please enter a valid email address.'
        }
    )

    # Password field with minimum length requirement
    password = forms.CharField(max_length=20, min_length=6)

    # Optional "Remember me" checkbox for persistent login
    remember = forms.BooleanField(required=False)




