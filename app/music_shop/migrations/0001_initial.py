# Generated by Django 5.0.3 on 2024-04-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductCard",
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
                ("image", models.CharField(max_length=200)),
                ("item_name", models.CharField(max_length=200)),
                ("cost", models.CharField(max_length=200)),
                ("info", models.CharField(max_length=200)),
            ],
        ),
    ]