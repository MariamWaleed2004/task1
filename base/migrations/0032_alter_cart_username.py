# Generated by Django 4.2.5 on 2023-10-31 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0031_alter_cart_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='username',
            field=models.ForeignKey(default='auth.User', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
