# Generated by Django 3.2.1 on 2021-05-08 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0003_alter_listing_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="listing",
            options={"ordering": ["-list_date"]},
        ),
    ]