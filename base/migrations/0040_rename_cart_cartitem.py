# Generated by Django 4.2.5 on 2023-11-02 14:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0039_cart_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='CartItem',
        ),
    ]
