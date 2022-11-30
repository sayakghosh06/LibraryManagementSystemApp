# Generated by Django 4.1.2 on 2022-11-17 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library_management", "0004_rename_id_memberadd_member_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Issuebook",
            fields=[
                ("Issue_id", models.IntegerField(primary_key=True, serialize=False)),
                ("Issuedate", models.DateField()),
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
