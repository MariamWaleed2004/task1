# Generated by Django 4.2.5 on 2023-10-30 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_order_cart_remove_order_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='username',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
