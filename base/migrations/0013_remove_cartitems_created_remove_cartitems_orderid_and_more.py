# Generated by Django 4.2.5 on 2023-10-28 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_cart_order_cartitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='created',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='orderId',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='shipped',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='totalOrderItemPrice',
        ),
    ]
