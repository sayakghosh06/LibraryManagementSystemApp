# Generated by Django 4.1.2 on 2022-11-17 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library_management", "0005_issuebook"),
    ]

    operations = [
        migrations.CreateModel(
            name="Returnbook",
            fields=[
                ("Return_id", models.IntegerField(primary_key=True, serialize=False)),
                ("Returndate", models.DateField()),
                ("Copies", models.IntegerField()),
                (
                    "Book_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="library_management.bookadd"
                    ),
                ),
                (
                    "Member_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="library_management.memberadd"
                    ),
                ),
            ],
        ),
    ]
