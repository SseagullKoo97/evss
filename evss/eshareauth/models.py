from django.db import models
from django.utils import timezone


# Model representing a Customer in the system
class Customer(models.Model):
    # Primary key field that auto-increments
    customer_id = models.AutoField(primary_key=True)
    # Unique email field for identifying the customer
    email = models.EmailField(unique=True)
    # Customer's full name, limited to 50 characters
    customer_name = models.CharField(max_length=50)
    # Date of birth for the customer
    dateofbirth = models.DateField()
    # Hashed password for the customer's account
    customer_password = models.CharField(max_length=255)
    # Optional field for customer's contact number
    customer_number = models.CharField(max_length=12, null=True)
    # One-to-one relationship with Wallet, allowing null and blank values
    wallet = models.OneToOneField(
        'Wallet',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='customer_wallet'
    )
    # Timestamp indicating when the customer account was created
    created_time = models.DateTimeField(default=timezone.now)
    # Boolean field to indicate if the customer is active
    is_active = models.BooleanField(default=True)

    class Meta:
        # Defines the table name in the database as 'customer'
        db_table = 'customer'

    # String representation for easier identification of customers in Django Admin
    def __str__(self):
        return self.email


# Model representing a Manager in the system
class Manager(models.Model):
    # Name of the manager
    manager_name = models.CharField(max_length=100)
    # Unique email field for identifying the manager
    manager_email = models.EmailField(unique=True)
    # Hashed password for the manager's account
    manager_password = models.CharField(max_length=255)
    # Optional field for manager's contact number
    manager_phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        # Defines the table name in the database as 'manager'
        db_table = 'manager'

    # String representation for easier identification of managers in Django Admin
    def __str__(self):
        return self.manager_email


# Model representing an Operator in the system
class Operator(models.Model):
    # Name of the operator
    operator_name = models.CharField(max_length=100)
    # Unique email field for identifying the operator
    operator_email = models.EmailField(unique=True)
    # Hashed password for the operator's account
    operator_password = models.CharField(max_length=255)
    # Optional field for operator's contact number
    operator_phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        # Defines the table name in the database as 'operator'
        db_table = 'operator'

    # String representation for easier identification of operators in Django Admin
    def __str__(self):
        return self.operator_email


# Model representing a Wallet associated with a Customer
class Wallet(models.Model):
    # Primary key field that auto-increments
    wallet_id = models.AutoField(primary_key=True)
    # Foreign key relationship to Customer, establishing a link to a specific customer
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
        related_name='customer_wallet'
    )
    # Balance in the wallet, with max 10 digits and 2 decimal places
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Optional field to store the payment method used by the customer
    payment_method = models.CharField(max_length=50, null=True)
    # Timestamp indicating the payment time
    payment_time = models.DateTimeField(null=True)

    class Meta:
        # Defines the table name in the database as 'wallet'
        db_table = 'wallet'

    # String representation for easier identification of wallets in Django Admin
    def __str__(self):
        return f"{self.customer.customer_name}'s Wallet"







