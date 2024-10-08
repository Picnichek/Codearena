# Generated by Django 5.0.7 on 2024-08-12 04:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("issues", "0002_issue_likes_comment_solution_solvedissue_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="name",
        ),
        migrations.AddField(
            model_name="issue",
            name="complexity",
            field=models.CharField(
                choices=[
                    ("Easy", "Easy"),
                    ("Medium", "Medium"),
                    ("Hard", "Hard"),
                ],
                default=123,
                help_text="Levels that are associated with the difficulty of finding a solution",
                max_length=15,
                verbose_name="Complexity",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tag",
            name="title",
            field=models.CharField(
                default=123,
                max_length=50,
                unique=True,
                verbose_name="Tag title",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="issue",
            name="likes",
            field=models.ManyToManyField(
                blank=True,
                help_text="User's likes to issue",
                related_name="issues",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Issue likes",
            ),
        ),
    ]
