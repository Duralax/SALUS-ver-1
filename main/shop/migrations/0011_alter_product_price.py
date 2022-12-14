# Generated by Django 4.1.2 on 2022-11-26 14:26

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Цена'),
        ),
    ]
