# Generated by Django 5.1.1 on 2024-10-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_coupon_expiry_date_alter_coupon_coupon_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='expiry_date',
            field=models.DateTimeField(),
        ),
    ]
