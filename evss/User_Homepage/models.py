
# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from eshareauth.models import Customer,Wallet
# 站点表
class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=100)  # 对应数据库中的 STATION_NAME 字段
    station_address = models.CharField(max_length=255)  # 对应数据库中的 STATION_ADDRESS 字段

    class Meta:
        db_table = 'station'
    def __str__(self):
        return self.station_name

# 车辆表
class Vehicle(models.Model):
    VEHICLE_STATUS_CHOICES = [
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Maintenance'),
        # Add more status choices as needed
    ]

    vehicle_id = models.AutoField(primary_key=True)  # SERIAL -> AutoField in Django
    vehicle_type = models.CharField(max_length=50)  # VARCHAR(50) -> CharField
    current_location = models.ForeignKey(
        'Station',  # Assuming 'Station' is another model representing the STATION table
        on_delete=models.CASCADE,  # Ensure referential integrity
        null=True,  # Allow NULL for the FK if required
        blank=True  # Optional, if current location can be empty
    )
    vehicle_status = models.CharField(
        max_length=50,
        choices=VEHICLE_STATUS_CHOICES,
        default='available'
    )
    battery_percentage = models.IntegerField(
        validators=[
            MinValueValidator(0),  # CHECK BATTERY_PERCENTAGE >= 0
            MaxValueValidator(100) # CHECK BATTERY_PERCENTAGE <= 100
        ]
    )
    class Meta:
        db_table = 'vehicle'

    def __str__(self):
        return f"{self.vehicle_type} (ID: {self.vehicle_id})"

class VehiclePricing(models.Model):
    pricing_id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=50)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.vehicle_type

    class Meta:
        db_table = 'vehicle_pricing'


# class Wallet(models.Model):
#     wallet_id = models.AutoField(primary_key=True)  # 等同于 SERIAL PRIMARY KEY
#     customer_id = models.IntegerField(unique=True,null=False)   # customer_id 的唯一约束
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # 十进制字段
#     payment_method = models.CharField(max_length=50, blank=True, null=True)  # VARCHAR(50)
#     payment_time = models.DateTimeField(blank=True, null=True)  # TIMESTAMP
#
#     class Meta:
#         db_table = 'wallet'  # 指定数据库表名（可选）
#     def __str__(self):
#         return f"Wallet {self.wallet_id}"


#顾客表
# class Customer(models.Model):
#     customer_id = models.AutoField(primary_key=True)
#     customer_name = models.CharField(max_length=50,null=False)
#     dateofbirth = models.DateField(null=False)
#     customer_password = models.CharField(max_length=255,null=False)
#     email = models.EmailField(max_length=100, unique=True,null=False)
#     customer_number = models.CharField(max_length=12,null=True)
#     wallet_id = models.ForeignKey(Wallet, on_delete=models.SET_NULL,null=True,blank=True,db_column='wallet_id')
#     created_time = models.DateTimeField(default=timezone.now)

    # class Meta:
    #     db_table = 'customer'
    # def __str__(self):
    #     return f"Customer {self.customer_id}"



#车辆订单表
class Rental(models.Model):
    RENTAL_STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    rental_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,db_column='customer_id',null=False)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE,db_column='vehicle_id',null=False)
    start_time = models.DateTimeField(default=timezone.now,null=False)
    end_time = models.DateTimeField(null=True, blank=True)
    rental_status = models.CharField(max_length=50, choices=RENTAL_STATUS_CHOICES, default='active')
    start_station_id = models.ForeignKey(Station, related_name='rental_start_station', on_delete=models.SET_NULL, null=True,db_column='start_station_id')
    end_station_id = models.ForeignKey(Station, related_name='rental_end_station', on_delete=models.SET_NULL, null=True,db_column='end_station_id')

    class Meta:
        db_table = 'rental'

    def __str__(self):
        return f"Rental {self.rental_id}"

