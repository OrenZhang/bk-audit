# Generated by Django 3.2.18 on 2023-04-26 09:03

import django.utils.timezone
from django.db import migrations, models

import core.models


class Migration(migrations.Migration):

    dependencies = [
        ("analyze", "0003_auto_20230407_1525"),
    ]

    operations = [
        migrations.CreateModel(
            name="ControlVersion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="创建时间")),
                ("created_by", models.CharField(default="", max_length=32, verbose_name="创建者")),
                ("updated_at", models.DateTimeField(blank=True, null=True, verbose_name="更新时间")),
                ("updated_by", models.CharField(blank=True, default="", max_length=32, verbose_name="修改者")),
                ("is_deleted", models.BooleanField(default=False, verbose_name="是否删除")),
                ("control_id", models.CharField(max_length=64, verbose_name="Control ID")),
                ("control_version", models.IntegerField(verbose_name="Control Version")),
                ("input_config", models.JSONField(default=dict, null=True, verbose_name="Input Config")),
                ("output_config", models.JSONField(default=dict, null=True, verbose_name="Output Config")),
                ("variable_config", models.JSONField(default=dict, null=True, verbose_name="Variable Config")),
                ("extra_config", models.JSONField(default=dict, null=True, verbose_name="Extra Config")),
            ],
            options={
                "verbose_name": "Control Version",
                "verbose_name_plural": "Control Version",
                "ordering": ["control_id", "-control_version"],
                "unique_together": {("control_id", "control_version")},
            },
        ),
        migrations.CreateModel(
            name="Control",
            fields=[
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="创建时间")),
                ("created_by", models.CharField(default="", max_length=32, verbose_name="创建者")),
                ("updated_at", models.DateTimeField(blank=True, null=True, verbose_name="更新时间")),
                ("updated_by", models.CharField(blank=True, default="", max_length=32, verbose_name="修改者")),
                ("is_deleted", models.BooleanField(default=False, verbose_name="是否删除")),
                (
                    "control_id",
                    core.models.UUIDField(
                        default=core.models.UUIDField.get_default_value,
                        max_length=64,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Control ID",
                    ),
                ),
                ("control_name", models.CharField(max_length=64, verbose_name="Control Name")),
                (
                    "control_type_id",
                    models.CharField(choices=[("BKM", "BK Monitor")], max_length=64, verbose_name="Control Type ID"),
                ),
            ],
            options={
                "verbose_name": "Control",
                "verbose_name_plural": "Control",
                "ordering": ["control_type_id", "control_id"],
                "unique_together": {("control_type_id", "control_name")},
            },
        ),
    ]
