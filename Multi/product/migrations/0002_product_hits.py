# Generated by Django 4.2.3 on 2023-08-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="hits",
            field=models.PositiveIntegerField(default=1, verbose_name="조회수"),
        ),
    ]
