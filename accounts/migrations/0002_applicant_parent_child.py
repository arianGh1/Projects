# Generated by Django 4.2.3 on 2023-07-24 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Applicant",
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
                ("name", models.CharField(max_length=120)),
                ("surname", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone_number", models.CharField(max_length=20, unique=True)),
                (
                    "resume",
                    models.FileField(blank=True, null=True, upload_to="resumes"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Parent",
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
                ("name", models.CharField(max_length=120)),
                ("surname", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone_number", models.CharField(max_length=20, unique=True)),
                ("username", models.CharField(blank=True, max_length=120)),
                ("password", models.CharField(blank=True, max_length=120)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Child",
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
                ("name", models.CharField(max_length=120)),
                ("surname", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone_number", models.CharField(max_length=20, unique=True)),
                ("fees_paid", models.DecimalField(decimal_places=3, max_digits=10)),
                ("fees_left", models.DecimalField(decimal_places=3, max_digits=10)),
                ("fee_due_date", models.DateField(blank=True, null=True)),
                ("last_paid_date", models.DateField(blank=True, null=True)),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.parent",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
