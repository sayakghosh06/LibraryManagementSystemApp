# Generated by Django 4.1.2 on 2022-11-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library_management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Memberadd",
            fields=[
                ("Member_Name", models.CharField(max_length=122)),
                ("Member_Address", models.CharField(max_length=122)),
                ("Phone", models.IntegerField()),
                ("id", models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]