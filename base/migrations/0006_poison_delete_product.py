# Generated by Django 4.2.3 on 2023-07-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('active', models.BooleanField(default=True)),
                ('category', models.CharField(blank=True, choices=[('Scorpion Poisons', 'Scorpion Poisons'), ('Sanke Poisons', 'Sanke Poisons'), ('Plant Toxins', 'Plant Toxins'), ('Animal Toxins', 'Animal Toxins')], max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
