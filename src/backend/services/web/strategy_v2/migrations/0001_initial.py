# Generated by Django 3.2.18 on 2023-04-26 09:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Strategy",
            fields=[
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="创建时间")),
                ("created_by", models.CharField(default="", max_length=32, verbose_name="创建者")),
                ("updated_at", models.DateTimeField(blank=True, null=True, verbose_name="更新时间")),
                ("updated_by", models.CharField(blank=True, default="", max_length=32, verbose_name="修改者")),
                ("is_deleted", models.BooleanField(default=False, verbose_name="是否删除")),
                ("namespace", models.CharField(max_length=64, verbose_name="Namespace")),
                ("strategy_id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="Strategy ID")),
                ("strategy_name", models.CharField(max_length=64, verbose_name="Strategy Name")),
                ("control_id", models.CharField(max_length=64, verbose_name="Control ID")),
                ("control_version", models.IntegerField(verbose_name="Version")),
                ("configs", models.JSONField(default=dict, verbose_name="Configs")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("disabled", "Disabled"),
                            ("failed", "Failed"),
                            ("pending", "Pending"),
                            ("running", "Running"),
                        ],
                        default="pending",
                        max_length=64,
                        verbose_name="Status",
                    ),
                ),
                ("backend_data", models.JSONField(default=dict, null=True, verbose_name="Backend Data")),
            ],
            options={
                "verbose_name": "Strategy",
                "verbose_name_plural": "Strategy",
                "ordering": ["control_id", "-strategy_id"],
            },
        ),
        migrations.CreateModel(
            name="StrategyTag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="创建时间")),
                ("created_by", models.CharField(default="", max_length=32, verbose_name="创建者")),
                ("updated_at", models.DateTimeField(blank=True, null=True, verbose_name="更新时间")),
                ("updated_by", models.CharField(blank=True, default="", max_length=32, verbose_name="修改者")),
                ("strategy_id", models.BigIntegerField(verbose_name="Strategy ID")),
                ("tag_id", models.BigIntegerField(verbose_name="Tag ID")),
            ],
            options={
                "verbose_name": "Strategy Tag",
                "verbose_name_plural": "Strategy Tag",
                "ordering": ["-id"],
            },
        ),
    ]
