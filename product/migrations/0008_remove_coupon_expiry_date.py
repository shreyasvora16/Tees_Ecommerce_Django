# Generated by Django 5.1.1 on 2024-10-04 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_coupon_expiry_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='expiry_date',
        ),
    ]
