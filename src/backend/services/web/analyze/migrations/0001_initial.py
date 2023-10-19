# Generated by Django 3.2.12 on 2023-02-13 10:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnalyzeConfig",
            fields=[
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="创建时间")),
                ("created_by", models.CharField(default="", max_length=32, verbose_name="创建者")),
                ("updated_at", models.DateTimeField(blank=True, null=True, verbose_name="更新时间")),
                ("updated_by", models.CharField(blank=True, default="", max_length=32, verbose_name="修改者")),
                ("is_deleted", models.BooleanField(default=False, verbose_name="是否删除")),
                ("analyze_id", models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name="分析ID")),
                (
                    "analyze_type",
                    models.CharField(
                        choices=[("regular", "常规"), ("aiops", "Aiops")], max_length=64, verbose_name="分析类型"
                    ),
                ),
                ("analyze_name", models.CharField(max_length=64, verbose_name="分析名称")),
                ("analyze_desc", models.TextField(blank=True, null=True, verbose_name="分析描述")),
                (
                    "status",
                    models.CharField(
                        choices=[("available", "可用"), ("draft", "草稿"), ("disabled", "禁用")],
                        max_length=64,
                        verbose_name="状态",
                    ),
                ),
                ("analyze_config", models.JSONField(blank=True, default=dict, null=True, verbose_name="分析配置")),
            ],
            options={
                "verbose_name": "分析能力配置",
                "verbose_name_plural": "分析能力配置",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="AnalyzeFieldConfig",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("analyze_id", models.CharField(db_index=True, max_length=64, verbose_name="分析ID")),
                ("field_name", models.CharField(max_length=64, verbose_name="字段名")),
                ("field_index", models.IntegerField(default=0, verbose_name="字段顺序")),
                ("field_alias", models.CharField(max_length=64, verbose_name="字段别名")),
                ("field_type", models.CharField(max_length=64, verbose_name="字段类型")),
                ("field_scope", models.JSONField(blank=True, default=list, null=True, verbose_name="字段范围")),
                (
                    "default_value",
                    models.JSONField(
                        blank=True, default=dict, help_text="字段含义，value(值)", null=True, verbose_name="默认值"
                    ),
                ),
                ("is_editable", models.BooleanField(default=True, verbose_name="是否可编辑")),
                ("is_display", models.BooleanField(default=True, verbose_name="是否展示")),
                (
                    "display_config",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="字段含义，component(前端组件), width(宽度), height(高度)",
                        null=True,
                        verbose_name="展示配置",
                    ),
                ),
                (
                    "validate_config",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="字段含义，required(是否必须), maxlength(字符串最大长度), minlength(字符串最小长度), max(数值最大值), min(数值最小值)",
                        null=True,
                        verbose_name="校验配置",
                    ),
                ),
            ],
            options={
                "verbose_name": "分析能力字段配置",
                "verbose_name_plural": "分析能力字段配置",
                "ordering": ["analyze_id", "field_index"],
                "unique_together": {("analyze_id", "field_name")},
            },
        ),
    ]
