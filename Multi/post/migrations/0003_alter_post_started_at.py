# Generated by Django 4.2.3 on 2023-08-13 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_alter_post_started_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="started_at",
            field=models.DateTimeField(blank=True, db_column="END_DATE", null=True),
        ),
    ]
