# Generated by Django 5.0.3 on 2024-10-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshareauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='id',
        ),
        migrations.AddField(
            model_name='wallet',
            name='wallet_id',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
