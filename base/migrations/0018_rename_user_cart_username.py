# Generated by Django 4.2.5 on 2023-10-30 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_rename_username_cart_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='username',
        ),
    ]