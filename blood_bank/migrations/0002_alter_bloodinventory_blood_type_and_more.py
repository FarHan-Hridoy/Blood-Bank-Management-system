# Generated by Django 5.1.3 on 2024-12-18 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blood_bank", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bloodinventory",
            name="blood_type",
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name="bloodinventory",
            name="capacity",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="bloodinventory",
            name="units",
            field=models.PositiveIntegerField(),
        ),
    ]
