# Generated by Django 4.2.3 on 2023-08-16 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_product_hits"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="hits",
        ),
    ]
