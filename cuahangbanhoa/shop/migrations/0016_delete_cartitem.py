# Generated by Django 5.0.7 on 2025-04-26 03:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0015_remove_cart_product_alter_cart_user_cartitem"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CartItem",
        ),
    ]
