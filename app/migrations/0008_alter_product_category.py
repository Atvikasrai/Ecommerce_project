# Generated by Django 5.0.1 on 2024-02-28 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_payment_orderplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('WT', 'Smartwatch'), ('SM', 'Smartphone'), ('LAP', 'Laptop')], max_length=3),
        ),
    ]
