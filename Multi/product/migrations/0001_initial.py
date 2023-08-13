# Generated by Django 4.2.3 on 2023-08-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=50)),
                ("lating", models.CharField(blank=True, max_length=50)),
                ("name", models.CharField(blank=True, max_length=50)),
                ("address", models.CharField(blank=True, max_length=50)),
                ("phoneNumber", models.CharField(blank=True, max_length=50)),
                ("re_time", models.TimeField(blank=True)),
                ("mo_time", models.TimeField(blank=True)),
                ("navi", models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
