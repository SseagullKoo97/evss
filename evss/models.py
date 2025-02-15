# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    dateofbirth = models.DateField()
    customer_password = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=100)
    customer_number = models.CharField(max_length=12, blank=True, null=True)
    wallet = models.ForeignKey('Wallet', models.DO_NOTHING, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    rental = models.ForeignKey('Rental', models.DO_NOTHING)
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    manager_name = models.CharField(max_length=100)
    manager_email = models.CharField(unique=True, max_length=100)
    manager_password = models.CharField(max_length=255)
    manager_phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'


class Operator(models.Model):
    operator_id = models.AutoField(primary_key=True)
    operator_name = models.CharField(max_length=100)
    operator_email = models.CharField(unique=True, max_length=100)
    operator_password = models.CharField(max_length=255)
    operator_phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operator'


class OperatorTasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    operator = models.ForeignKey(Operator, models.DO_NOTHING)
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING)
    task_type = models.CharField(max_length=50)
    task_completed_time = models.DateTimeField(blank=True, null=True)
    movement_destination = models.ForeignKey('Station', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operator_tasks'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    wallet = models.ForeignKey('Wallet', models.DO_NOTHING)
    rental = models.ForeignKey('Rental', models.DO_NOTHING)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    rental_status = models.CharField(max_length=50, blank=True, null=True)
    start_station = models.ForeignKey('Station', models.DO_NOTHING, blank=True, null=True)
    end_station = models.ForeignKey('Station', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rental'


class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=100)
    station_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    current_location = models.ForeignKey(Station, models.DO_NOTHING, blank=True, null=True)
    vehicle_status = models.CharField(max_length=50, blank=True, null=True)
    battery_percentage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle'


class VehicleMaintenance(models.Model):
    maintenance_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, models.DO_NOTHING)
    operator = models.ForeignKey(Operator, models.DO_NOTHING)
    issue_description = models.CharField(max_length=255, blank=True, null=True)
    bell_condition = models.BooleanField(blank=True, null=True)
    handle_condition = models.BooleanField(blank=True, null=True)
    tyre_condition = models.BooleanField(blank=True, null=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_maintenance'


class VehiclePricing(models.Model):
    pricing_id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=50)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_pricing'


class Wallet(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    payment_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet'
