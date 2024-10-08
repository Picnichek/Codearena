# Generated by Django 5.0.7 on 2024-08-05 11:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import django_extensions.db.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True,
                        verbose_name="modified",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="Tag name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True,
                        verbose_name="modified",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=50, verbose_name="Title"),
                ),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "hint",
                    models.TextField(
                        blank=True,
                        help_text="A hint that will push the user towards solving the issue",
                        verbose_name="Hint",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        help_text="Tags that attached with issue",
                        related_name="issues",
                        to="issues.tag",
                        verbose_name="Issue tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "Issue",
                "verbose_name_plural": "Issues",
            },
        ),
        migrations.CreateModel(
            name="TestCase",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True,
                        verbose_name="modified",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[("Python", "Python")],
                        default="Python",
                        max_length=30,
                        verbose_name="Language",
                    ),
                ),
                ("input_data", models.TextField(verbose_name="Input data")),
                (
                    "excepted_output",
                    models.TextField(verbose_name="Excepted output"),
                ),
                (
                    "order",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
                (
                    "allocated_time",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(3),
                            django.core.validators.MaxValueValidator(6),
                        ],
                        verbose_name="Allocated time(seconds)",
                    ),
                ),
                (
                    "allocated_memory",
                    models.IntegerField(
                        default=128,
                        validators=[
                            django.core.validators.MinValueValidator(8),
                            django.core.validators.MaxValueValidator(256),
                        ],
                        verbose_name="Allocated memory(mb)",
                    ),
                ),
                (
                    "issue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="test_cases",
                        to="issues.issue",
                        verbose_name="Issue id",
                    ),
                ),
            ],
            options={
                "verbose_name": "Test case",
                "verbose_name_plural": "Test cases",
            },
        ),
        migrations.AddConstraint(
            model_name="testcase",
            constraint=models.UniqueConstraint(
                fields=("issue", "order"),
                name="unique_task_order",
            ),
        ),
    ]
