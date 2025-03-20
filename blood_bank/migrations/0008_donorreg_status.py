# Generated by Django 5.1.3 on 2024-12-21 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blood_bank", "0007_donorreg_last_donation_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="donorreg",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=10,
            ),
        ),
    ]
