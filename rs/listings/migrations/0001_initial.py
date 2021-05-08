# Generated by Django 3.2.1 on 2021-05-08 15:53

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("realtors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Listing",
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
                ("title", models.CharField(max_length=200, verbose_name="title")),
                ("address", models.CharField(max_length=200, verbose_name="address")),
                ("city", models.CharField(max_length=100, verbose_name="city")),
                ("state", models.CharField(max_length=100, verbose_name="state")),
                ("zipcode", models.CharField(max_length=20, verbose_name="zip code")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                ("price", models.IntegerField(verbose_name="price")),
                ("bedrooms", models.IntegerField(verbose_name="bedrooms")),
                (
                    "bathrooms",
                    models.DecimalField(
                        decimal_places=1, max_digits=2, verbose_name="bathroms"
                    ),
                ),
                ("garage", models.IntegerField(default=0, verbose_name="garage")),
                ("sqft", models.IntegerField(verbose_name="sqft")),
                (
                    "lot_size",
                    models.DecimalField(
                        decimal_places=1, max_digits=5, verbose_name="lot size"
                    ),
                ),
                (
                    "photo_main",
                    models.ImageField(
                        upload_to="photos/%Y/%m/%d/", verbose_name="photo main"
                    ),
                ),
                (
                    "photo_1",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_2",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_3",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_4",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_5",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_6",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="is published?"),
                ),
                (
                    "list_date",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime.now,
                        verbose_name="list date",
                    ),
                ),
                (
                    "realter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="realtors.realtor",
                    ),
                ),
            ],
        ),
    ]