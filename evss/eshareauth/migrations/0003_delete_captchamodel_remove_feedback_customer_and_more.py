# Generated by Django 5.0.3 on 2024-10-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshareauth', '0002_remove_wallet_id_wallet_wallet_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CaptchaModel',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='rental',
        ),
        migrations.RemoveField(
            model_name='vehiclemaintenance',
            name='operator',
        ),
        migrations.RemoveField(
            model_name='operatortasks',
            name='operator',
        ),
        migrations.RemoveField(
            model_name='operatortasks',
            name='movement_destination',
        ),
        migrations.RemoveField(
            model_name='operatortasks',
            name='vehicle',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='rental',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='wallet',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='end_station',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='start_station',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='vehicle',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='current_location',
        ),
        migrations.RemoveField(
            model_name='vehiclemaintenance',
            name='vehicle',
        ),
        migrations.DeleteModel(
            name='VehiclePricing',
        ),
        migrations.AlterField(
            model_name='manager',
            name='manager_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Operator',
        ),
        migrations.DeleteModel(
            name='OperatorTasks',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
        migrations.DeleteModel(
            name='Station',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
        migrations.DeleteModel(
            name='VehicleMaintenance',
        ),
    ]
